/**
 * beBriz License Key Generator & Validator
 * ==========================================
 * Shared checksum algorithm — must match generate_keys.py and Theme.License in theme.js.
 *
 * Key format: BEBRIZ-{THEME_CODE}-{RANDOM8}-{CHECKSUM4}
 *   THEME_CODE: 4-char code (LUXF, LUXI, LUXT, LUXG)
 *   RANDOM8:    8 alphanumeric chars (uppercase)
 *   CHECKSUM4:  4-char base36 hash
 */

var BeBrizKeygen = (function () {
  'use strict';

  var THEME_CODES = {
    'luxe-fashion':  'LUXF',
    'luxe-interior': 'LUXI',
    'luxe-tech':     'LUXT',
    'luxe-gourmet':  'LUXG'
  };

  var THEME_HANDLES = {};
  Object.keys(THEME_CODES).forEach(function (handle) {
    THEME_HANDLES[THEME_CODES[handle]] = handle;
  });

  var CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';

  /**
   * Compute the 4-char checksum for a key prefix.
   * Algorithm: sum of (charCode * (position + 1)) for each char in prefix,
   * mod 1679616 (36^4), converted to base36 uppercase, zero-padded to 4 chars.
   *
   * @param {string} prefix — e.g. "BEBRIZ-LUXF-A1B2C3D4"
   * @returns {string} 4-char checksum
   */
  function computeChecksum(prefix) {
    var sum = 0;
    for (var i = 0; i < prefix.length; i++) {
      sum += prefix.charCodeAt(i) * (i + 1);
    }
    var mod = sum % 1679616; // 36^4
    var hash = mod.toString(36).toUpperCase();
    while (hash.length < 4) {
      hash = '0' + hash;
    }
    return hash;
  }

  /**
   * Generate a random alphanumeric string of given length.
   */
  function randomString(len) {
    var result = '';
    for (var i = 0; i < len; i++) {
      result += CHARS.charAt(Math.floor(Math.random() * CHARS.length));
    }
    return result;
  }

  /**
   * Get the 4-char theme code from a theme handle.
   * @param {string} handle — e.g. "luxe-fashion"
   * @returns {string|null}
   */
  function getThemeCode(handle) {
    return THEME_CODES[handle] || null;
  }

  /**
   * Get the theme handle from a 4-char code.
   * @param {string} code — e.g. "LUXF"
   * @returns {string|null}
   */
  function getThemeHandle(code) {
    return THEME_HANDLES[code] || null;
  }

  /**
   * Generate a new license key.
   * @param {string} themeHandle — e.g. "luxe-fashion"
   * @param {string} email
   * @returns {{ key: string, record: Object }|null}
   */
  function generateKey(themeHandle, email) {
    var code = getThemeCode(themeHandle);
    if (!code) return null;

    var random = randomString(8);
    var prefix = 'BEBRIZ-' + code + '-' + random;
    var checksum = computeChecksum(prefix);
    var key = prefix + '-' + checksum;

    var today = new Date();
    var dateStr = today.getFullYear() + '-' +
      String(today.getMonth() + 1).padStart(2, '0') + '-' +
      String(today.getDate()).padStart(2, '0');

    var record = {
      key: key,
      theme: themeHandle,
      email: email || '',
      domain: null,
      dev_domain: null,
      created: dateStr,
      activated: null,
      status: 'active'
    };

    return { key: key, record: record };
  }

  /**
   * Validate a license key format and checksum.
   * @param {string} key
   * @returns {{ valid: boolean, themeCode: string|null, themeHandle: string|null }}
   */
  function validateKey(key) {
    if (!key || typeof key !== 'string') {
      return { valid: false, themeCode: null, themeHandle: null };
    }

    key = key.trim().toUpperCase();

    // Must match BEBRIZ-XXXX-XXXXXXXX-XXXX
    var pattern = /^BEBRIZ-([A-Z0-9]{4})-([A-Z0-9]{8})-([A-Z0-9]{4})$/;
    var match = key.match(pattern);
    if (!match) {
      return { valid: false, themeCode: null, themeHandle: null };
    }

    var themeCode = match[1];
    var checksum = match[3];
    var prefix = 'BEBRIZ-' + themeCode + '-' + match[2];
    var expected = computeChecksum(prefix);

    if (checksum !== expected) {
      return { valid: false, themeCode: themeCode, themeHandle: getThemeHandle(themeCode) };
    }

    return {
      valid: true,
      themeCode: themeCode,
      themeHandle: getThemeHandle(themeCode)
    };
  }

  return {
    generateKey: generateKey,
    validateKey: validateKey,
    getThemeCode: getThemeCode,
    getThemeHandle: getThemeHandle,
    computeChecksum: computeChecksum,
    THEME_CODES: THEME_CODES
  };

})();

// Export for Node.js if available
if (typeof module !== 'undefined' && module.exports) {
  module.exports = BeBrizKeygen;
}
