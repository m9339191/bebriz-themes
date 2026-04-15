/* ========================================
   beBriz Premium Theme Store
   Main JavaScript
   ======================================== */

document.addEventListener('DOMContentLoaded', function () {

  /* ----------------------------------------
     Mobile Navigation Toggle
     ---------------------------------------- */
  var toggle = document.querySelector('.mobile-toggle');
  var navLinks = document.querySelector('.nav-links');

  if (toggle && navLinks) {
    toggle.addEventListener('click', function () {
      var isOpen = navLinks.classList.toggle('open');
      toggle.classList.toggle('active', isOpen);
      toggle.setAttribute('aria-expanded', isOpen);
      // Prevent body scroll when mobile nav is open
      document.body.style.overflow = isOpen ? 'hidden' : '';
    });

    // Close nav when a link is clicked
    navLinks.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        navLinks.classList.remove('open');
        toggle.classList.remove('active');
        toggle.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      });
    });
  }

  /* ----------------------------------------
     Scroll Reveal (IntersectionObserver)
     ---------------------------------------- */
  var revealElements = document.querySelectorAll('.reveal');

  if (revealElements.length && 'IntersectionObserver' in window) {
    var revealObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          revealObserver.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.1,
      rootMargin: '0px 0px -40px 0px'
    });

    revealElements.forEach(function (el) {
      revealObserver.observe(el);
    });
  } else {
    // Fallback: show all elements
    revealElements.forEach(function (el) {
      el.classList.add('visible');
    });
  }

  /* ----------------------------------------
     Header Background on Scroll
     ---------------------------------------- */
  var header = document.querySelector('.site-header');

  if (header) {
    function updateHeader() {
      if (window.scrollY > 20) {
        header.style.background = 'rgba(10,10,11,0.95)';
      } else {
        header.style.background = 'rgba(10,10,11,0.8)';
      }
    }

    window.addEventListener('scroll', updateHeader, { passive: true });
    updateHeader();
  }

  /* ----------------------------------------
     Accordion
     ---------------------------------------- */
  document.querySelectorAll('.accordion-trigger').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var item = btn.closest('.accordion-item');
      var isActive = item.classList.contains('active');
      var parent = item.parentElement;

      // Close siblings
      parent.querySelectorAll('.accordion-item.active').forEach(function (open) {
        if (open !== item) {
          open.classList.remove('active');
        }
      });

      item.classList.toggle('active', !isActive);
    });
  });

  /* ----------------------------------------
     Docs Sidebar Toggle (mobile)
     ---------------------------------------- */
  var sidebarToggle = document.querySelector('.docs-sidebar-toggle');
  var sidebar = document.querySelector('.docs-sidebar');

  if (sidebarToggle && sidebar) {
    sidebarToggle.addEventListener('click', function () {
      var isOpen = sidebar.classList.toggle('open');
      sidebarToggle.textContent = isOpen ? 'Hide Navigation' : 'Show Navigation';
    });
  }

  /* ----------------------------------------
     Docs Sidebar Active State on Scroll
     ---------------------------------------- */
  var docsSections = document.querySelectorAll('.docs-content h2[id]');
  var docsLinks = document.querySelectorAll('.docs-sidebar nav a');

  if (docsSections.length && docsLinks.length) {
    function updateActiveLink() {
      var scrollY = window.scrollY + 120;
      var current = '';

      docsSections.forEach(function (section) {
        if (section.offsetTop <= scrollY) {
          current = section.getAttribute('id');
        }
      });

      docsLinks.forEach(function (link) {
        link.classList.remove('active');
        if (link.getAttribute('href') === '#' + current) {
          link.classList.add('active');
        }
      });
    }

    window.addEventListener('scroll', updateActiveLink, { passive: true });
    updateActiveLink();
  }

  /* ----------------------------------------
     Smooth Scroll for Anchor Links
     ---------------------------------------- */
  document.querySelectorAll('a[href^="#"]').forEach(function (link) {
    link.addEventListener('click', function (e) {
      var href = link.getAttribute('href');
      if (href === '#') return;

      var target = document.querySelector(href);
      if (target) {
        e.preventDefault();

        var offset = 90; // account for fixed header
        var targetPos = target.getBoundingClientRect().top + window.scrollY - offset;

        window.scrollTo({
          top: targetPos,
          behavior: 'smooth'
        });

        // Close mobile sidebar if open
        if (sidebar && sidebar.classList.contains('open')) {
          sidebar.classList.remove('open');
          if (sidebarToggle) {
            sidebarToggle.textContent = 'Show Navigation';
          }
        }
      }
    });
  });

  /* ----------------------------------------
     Contact Form Handler (placeholder)
     ---------------------------------------- */
  var contactForm = document.querySelector('.contact-form');

  if (contactForm) {
    contactForm.addEventListener('submit', function (e) {
      e.preventDefault();
      var btn = contactForm.querySelector('button[type="submit"]');

      if (btn) {
        var original = btn.textContent;
        btn.textContent = 'Message Sent!';
        btn.classList.add('loading');
        btn.disabled = true;

        setTimeout(function () {
          btn.textContent = original;
          btn.classList.remove('loading');
          btn.disabled = false;
          contactForm.reset();
        }, 2500);
      }
    });
  }

  /* ----------------------------------------
     Parallax-like subtle movement on hero
     ---------------------------------------- */
  var hero = document.querySelector('.hero');

  if (hero && window.innerWidth > 768) {
    window.addEventListener('scroll', function () {
      var scrolled = window.scrollY;
      var heroContent = hero.querySelector('.hero-content');
      if (heroContent && scrolled < window.innerHeight) {
        heroContent.style.transform = 'translateY(' + (scrolled * 0.15) + 'px)';
        heroContent.style.opacity = 1 - (scrolled / (window.innerHeight * 0.8));
      }
    }, { passive: true });
  }

  /* ----------------------------------------
     Staggered animation for grid children
     ---------------------------------------- */
  var staggerContainers = document.querySelectorAll('.stagger-children');

  if (staggerContainers.length && 'IntersectionObserver' in window) {
    var staggerObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          var children = entry.target.children;
          Array.prototype.forEach.call(children, function (child, index) {
            child.style.transitionDelay = (index * 0.08) + 's';
            child.classList.add('visible');
          });
          staggerObserver.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.1,
      rootMargin: '0px 0px -20px 0px'
    });

    staggerContainers.forEach(function (container) {
      // Set initial hidden state on children
      Array.prototype.forEach.call(container.children, function (child) {
        child.style.opacity = '0';
        child.style.transform = 'translateY(20px)';
        child.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
      });
      staggerObserver.observe(container);
    });
  }

  /* ----------------------------------------
     Visible class for stagger children
     ---------------------------------------- */
  // The CSS for .visible on stagger children is handled inline above

  /* ----------------------------------------
     Catalog Category Filter
     ---------------------------------------- */
  var filterBtns = document.querySelectorAll('.catalog-filter');
  var catalogCards = document.querySelectorAll('.catalog-card');

  if (filterBtns.length && catalogCards.length) {
    function applyFilter(filter) {
      catalogCards.forEach(function (card) {
        var category = card.getAttribute('data-category');
        if (filter === 'all' || category === filter) {
          card.style.display = '';
        } else {
          card.style.display = 'none';
        }
      });
    }

    filterBtns.forEach(function (btn) {
      btn.addEventListener('click', function () {
        var filter = btn.getAttribute('data-filter');
        filterBtns.forEach(function (b) { b.classList.remove('is-active'); });
        btn.classList.add('is-active');
        applyFilter(filter);
      });
    });

    // Apply initial filter on page load
    var activeBtn = document.querySelector('.catalog-filter.is-active');
    if (activeBtn) {
      applyFilter(activeBtn.getAttribute('data-filter'));
    }
  }

  // ===== Image Lightbox =====
  var previewImages = document.querySelectorAll('.preview-card img');
  if (previewImages.length > 0) {
    var lightbox = document.createElement('div');
    lightbox.className = 'lightbox';
    lightbox.setAttribute('aria-hidden', 'true');

    var closeBtn = document.createElement('button');
    closeBtn.className = 'lightbox__close';
    closeBtn.setAttribute('aria-label', 'Close');
    closeBtn.textContent = '\u00D7';
    lightbox.appendChild(closeBtn);

    var prevBtn = document.createElement('button');
    prevBtn.className = 'lightbox__prev';
    prevBtn.setAttribute('aria-label', 'Previous');
    prevBtn.textContent = '\u2039';
    lightbox.appendChild(prevBtn);

    var nextBtn = document.createElement('button');
    nextBtn.className = 'lightbox__next';
    nextBtn.setAttribute('aria-label', 'Next');
    nextBtn.textContent = '\u203A';
    lightbox.appendChild(nextBtn);

    var content = document.createElement('div');
    content.className = 'lightbox__content';
    var lightboxImg = document.createElement('img');
    lightboxImg.className = 'lightbox__img';
    lightboxImg.alt = '';
    content.appendChild(lightboxImg);
    var lightboxCaption = document.createElement('div');
    lightboxCaption.className = 'lightbox__caption';
    content.appendChild(lightboxCaption);
    lightbox.appendChild(content);

    document.body.appendChild(lightbox);

    var currentIndex = 0;
    var imageList = Array.prototype.slice.call(previewImages);

    function openLightbox(index) {
      currentIndex = index;
      var img = imageList[index];
      lightboxImg.src = img.src;
      lightboxImg.alt = img.alt || '';
      var card = img.closest('.preview-card');
      var label = card ? card.querySelector('.preview-label') : null;
      lightboxCaption.textContent = label ? label.textContent : '';
      lightbox.classList.add('is-open');
      lightbox.setAttribute('aria-hidden', 'false');
      document.body.style.overflow = 'hidden';
    }

    function closeLightbox() {
      lightbox.classList.remove('is-open');
      lightbox.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
    }

    function showNext() {
      openLightbox((currentIndex + 1) % imageList.length);
    }

    function showPrev() {
      openLightbox((currentIndex - 1 + imageList.length) % imageList.length);
    }

    imageList.forEach(function (img, i) {
      img.style.cursor = 'zoom-in';
      img.addEventListener('click', function () { openLightbox(i); });
    });

    closeBtn.addEventListener('click', closeLightbox);
    nextBtn.addEventListener('click', function (e) { e.stopPropagation(); showNext(); });
    prevBtn.addEventListener('click', function (e) { e.stopPropagation(); showPrev(); });
    lightbox.addEventListener('click', function (e) {
      if (e.target === lightbox || e.target === content) closeLightbox();
    });
    document.addEventListener('keydown', function (e) {
      if (!lightbox.classList.contains('is-open')) return;
      if (e.key === 'Escape') closeLightbox();
      if (e.key === 'ArrowRight') showNext();
      if (e.key === 'ArrowLeft') showPrev();
    });
  }

});
