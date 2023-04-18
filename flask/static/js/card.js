$(document).ready(function () {
    let current_fs, next_fs, previous_fs; //fieldsets
    let opacity;
    let current = 1;
    let steps = $("fieldset").length;
    window.type = "all";
    window.class = "all";
    window.rarity = "all";

    setProgressBar(current);

    $(".inputGroup").click(function (e) {
        if (e.target.tagName === "INPUT") {
            if (e.target.name === "type") {
                window.type = e.target.value;
            }
            if (e.target.name === "class") {
                window.class = e.target.value;
            }
            if (e.target.name === "rarity") {
                window.rarity = e.target.value;
            }
        }
    })

    $(".next").click(function () {
        current_fs = $(this).parent();
        next_fs = $(this).parent().next();

        //show the next fieldset
        next_fs.show();
        //hide the current fieldset with style
        current_fs.animate(
            { opacity: 0 },
            {
                step: function (now) {
                    // for making fielset appear animation
                    opacity = 1 - now;

                    current_fs.css({
                        display: "none",
                        position: "relative",
                    });
                    next_fs.css({ opacity: opacity });
                },
                duration: 500,
            }
        );
        setProgressBar(++current);
    });

    function setProgressBar(curStep) {
        var percent = parseFloat(100 / steps) * curStep;
        percent = percent.toFixed();
        $(".progress-bar").css("width", percent + "%");
    }

    $(".submit").click(function () {
        return false;
    });
});
