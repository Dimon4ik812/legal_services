jQuery(function ($) {
    'use strict';

	// START MENU JS
	$(window).on('scroll', function() {
		if ($(this).scrollTop() > 50) {
			$('.main-nav').addClass('menu-shrink');
		} else {
			$('.main-nav').removeClass('menu-shrink');
		}
	});				

    // Mean Menu
	jQuery('.mean-menu').meanmenu({
		meanScreenWidth: "991"
	});

	// Home Slider JS
	$('.home-slider').owlCarousel({
		items: 1,
		loop:true,
		margin: 0,
		nav: true,
		rtl: true,
		dots: true,
		smartSpeed: 1000,
		autoplay:true,
		autoplayTimeout:4000,
		autoplayHoverPause:true,
		navText: [
			"<i class='icofont-simple-left'></i>",
			"<i class='icofont-simple-right'></i>"
		]
	});

	// Popup Youtube JS
	$('.popup-youtube').magnificPopup({
		disableOn: 700,
		type: 'iframe',
		mainClass: 'mfp-fade',
		removalDelay: 160,
		preloader: false,
		fixedContentPos: false
	});

	// Blog Slider JS
	$('.blog-slider').owlCarousel({
		loop:true,
		margin: 0,
		nav: false,
		rtl: true,
		dots: true,
		smartSpeed: 1000,
		autoplay:true,
		autoplayTimeout:3000,
		autoplayHoverPause:true,
		responsive:{
			0:{
				items:1,
			},
			600:{
				items:1,
			},
			800:{
				items:2,
			},
			1000:{
				items:3,
			}
		}
	});

	// Wow JS
	new WOW().init();

	// Odometer JS
	$('.odometer').appear(function(e) {
		var odo = $('.odometer');
		odo.each(function() {
			var countNumber = $(this).attr('data-count');
			$(this).html(countNumber);
		});
	});

	// Nice Select JS
	$('select').niceSelect();

	// Subscribe form
	$(".newsletter-form").validator().on("submit", function (event) {
		if (event.isDefaultPrevented()) {
		// handle the invalid form...
		formErrorSub();
		submitMSGSub(false, "Please enter your email correctly.");
		} else {
		// everything looks good!
		event.preventDefault();
		}
	});
	function callbackFunction (resp) {
		if (resp.result === "success") {
		formSuccessSub();
		}
		else {
		formErrorSub();
		}
	}
	function formSuccessSub(){
		$(".newsletter-form")[0].reset();
		submitMSGSub(true, "Thank you for subscribing!");
		setTimeout(function() {
		$("#validator-newsletter").addClass('hide');
		}, 4000)
	}
	function formErrorSub(){
		$(".newsletter-form").addClass("animated shake");
		setTimeout(function() {
		$(".newsletter-form").removeClass("animated shake");
		}, 1000)
	}
	function submitMSGSub(valid, msg){
		if(valid){
		var msgClasses = "validation-success";
		} else {
		var msgClasses = "validation-danger";
		}
		$("#validator-newsletter").removeClass().addClass(msgClasses).text(msg);
	}
	
	// AJAX MailChimp
	$(".newsletter-form").ajaxChimp({
		url: "https://envytheme.us20.list-manage.com/subscribe/post?u=60e1ffe2e8a68ce1204cd39a5&amp;id=42d6d188d9", // Your url MailChimp
		callback: callbackFunction
	});

	// Accordion JS
	$('.accordion > li:eq(0) a').addClass('active').next().slideDown();
	$('.accordion a').on('click', function(j) {
		var dropDown = $(this).closest('li').find('p');
		$(this).closest('.accordion').find('p').not(dropDown).slideUp(300);
		if ($(this).hasClass('active')) {
			$(this).removeClass('active');
		} else {
			$(this).closest('.accordion').find('a.active').removeClass('active');
			$(this).addClass('active');
		}
		dropDown.stop(false, true).slideToggle(300);
		j.preventDefault();
	});

	// Back to top 
	$('body').append('<div id="toTop" class="back-to-top-btn"><i class="icofont-bubble-up"></i></div>');
	$(window).scroll(function () {
		if ($(this).scrollTop() != 0) {
			$('#toTop').fadeIn();
		} else {
			$('#toTop').fadeOut();
		}
	}); 
	$('#toTop').on('click', function(){
		$("html, body").animate({ scrollTop: 0 }, 900);
		return false;
	});

	// PRELOADER
	jQuery(window).on('load',function(){
		jQuery(".loader").fadeOut(500);
	});

}(jQuery));

document.addEventListener("DOMContentLoaded", function () {
        console.log("Bootstrap Modal:", typeof bootstrap.Modal);
        if (typeof bootstrap.Modal === 'function') {
            console.log("✅ Bootstrap JS работает");
        } else {
            console.log("❌ Bootstrap JS не загружен или повреждён");
        }
    });

function testModal() {
    const el = document.getElementById('consultationModal');
    if (!el) {
        console.error('Модальное окно не найдено');
        return;
    }
    const modal = new bootstrap.Modal(el);
    modal.show();
    console.log('Модальное окно открыто');
}

document.addEventListener("DOMContentLoaded", function () {
    // Показать модальное окно через 30 секунд
    setTimeout(function () {
      const modal = new bootstrap.Modal(document.getElementById('consultationModal'));
      modal.show();
      // Автофокус на поле ввода
      document.getElementById('phone').focus();
    }, 30000);

    // Отправка формы
    document.getElementById('submitConsultation').addEventListener('click', function () {
      const phone = document.getElementById('phone').value;

      if (phone) {
        // Отправка в Telegram
        sendToTelegram(phone);

        // Успешное сообщение
        alert('Спасибо! Мы скоро вам перезвоним.');
        const modal = bootstrap.Modal.getInstance(document.getElementById('consultationModal'));
        modal.hide();
        document.getElementById('consultationForm').reset();
      } else {
        alert('Пожалуйста, введите номер телефона');
      }
    });

    // Функция отправки в Telegram
    function sendToTelegram(phone) {
      const { botToken, chatId } = TELEGRAM_CONFIG;     // ← Замените на ваш ID
      const message = `📞 Новый запрос на консультацию:\nНомер: ${phone}`;

      fetch(`https://api.telegram.org/bot${botToken}/sendMessage`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          chat_id: chatId,
          text: message
        })
      }).catch(err => console.error('Ошибка отправки в Telegram:', err));
    }
  });