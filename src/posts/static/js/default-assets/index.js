(function ($) {
    'use strict';

    var roberto_window = $(window);

    // ****************************
    // :: 1.0 Preloader Active Code
    // ****************************

    roberto_window.on('load', function () {
        $('#preloader').fadeOut('1000', function () {
            $(this).remove();
        });
    });

    // *********************************
    // :: 4.0 Welcome Slides Active Code
    // *********************************

    if ($.fn.owlCarousel) {
        var welcomeSlider = $('.welcome-slides');
        welcomeSlider.owlCarousel({
            items: 1,
            loop: true,
            autoplay: true,
            smartSpeed: 1000,
            autoplayTimeout:10000,
            nav: true
        })

        welcomeSlider.on('translate.owl.carousel', function () {
            var layer = $("[data-animation]");
            layer.each(function () {
                var anim_name = $(this).data('animation');
                $(this).removeClass('animated ' + anim_name).css('opacity', '0');
            });
        });

        $("[data-delay]").each(function () {
            var anim_del = $(this).data('delay');
            $(this).css('animation-delay', anim_del);
        });

        $("[data-duration]").each(function () {
            var anim_dur = $(this).data('duration');
            $(this).css('animation-duration', anim_dur);
        });

        welcomeSlider.on('translated.owl.carousel', function () {
            var layer = welcomeSlider.find('.owl-item.active').find("[data-animation]");
            layer.each(function () {
                var anim_name = $(this).data('animation');
                $(this).addClass('animated ' + anim_name).css('opacity', '1');
            });
        });

        function welcomeSlide() {
            $('.owl-item').removeClass('prev next');
            var currentSlide = $('.welcome-slides .owl-item.active');
            currentSlide.next('.owl-item').addClass('next');
            currentSlide.prev('.owl-item').addClass('prev');
            var nextSlideImg = $('.owl-item.next').find('.single-welcome-slide').attr('data-img-url');
            var prevSlideImg = $('.owl-item.prev').find('.single-welcome-slide').attr('data-img-url');
            $('.owl-nav .owl-prev').css({
                background: 'url(' + prevSlideImg + ')'
            });
            $('.owl-nav .owl-next').css({
                background: 'url(' + nextSlideImg + ')'
            });
        }

        welcomeSlide();

        welcomeSlider.on('translated.owl.carousel', function () {
            welcomeSlide();
        });
    }
    // ******************************
    // :: 18.0 Datepicker Active Code
    // ******************************
    if ($.fn.datepicker) {
        $('.input-daterange').datepicker({
            format: "dd/mm/yy",
            multidate: true,
            keyboardNavigation: false,
            forceParse: false,
            daysOfWeekHighlighted: "0,1,2,3,4,5,6",
            todayHighlight: true
        });
    }

    // ********************************
    // :: 19.0 Range Slider Active Code
    // ********************************
    $('.slider-range-price').each(function () {
        var min = jQuery(this).data('min');
        var max = jQuery(this).data('max');
        var unit = jQuery(this).data('unit');
        var value_min = jQuery(this).data('value-min');
        var value_max = jQuery(this).data('value-max');
        var label_result = jQuery(this).data('label-result');
        var t = $(this);
        $(this).slider({
            range: true,
            min: min,
            max: max,
            values: [value_min, value_max],
            slide: function (event, ui) {
                var result = label_result + " " + unit + ui.values[0] + ' - ' + unit + ui.values[1];
                console.log(t);
                t.closest('.slider-range').find('.range-price').html(result);
            }
        });
    })
})(jQuery);