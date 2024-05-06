$(document).ready(function () {
    function fetchTranslation() {
        let languageCode = $("#language_code").val();
        let apiUrl = "https://www.fourtonfish.com/hellosalut/hello/?lang=" + languageCode;

        $.ajax({
            url: apiUrl,
            type: "GET",
            success: function (data) {
                $("#hello").text(data.hello);
            },
            error: function () {
                $("#hello").text("Error: Translation not available");
            }
        });
    }

    $("#btn_translate").click(fetchTranslation);

    $("#language_code").keypress(function (event) {
        if (event.keyCode === 13) {
            fetchTranslation();
        }
    });
});
