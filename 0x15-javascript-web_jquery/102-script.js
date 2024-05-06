$(document).ready(function () {
    $("#btn_translate").click(function () {
        var languageCode = $("#language_code").val();
        var apiUrl = "https://www.fourtonfish.com/hellosalut/hello/?lang=" + languageCode;

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
    });
});
