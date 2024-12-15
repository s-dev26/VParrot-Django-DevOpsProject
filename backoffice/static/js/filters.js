$(document).ready(function () {
  $("#filters_form").on("submit", function (e) {
    e.preventDefault();

    var formData = $(this).serialize();
    console.log("FormData:", formData);

    $.ajax({
      type: "POST",
      url: "filter_cars/",
      data: formData,
      success: function (data) {
        $("#cars ul").html("");

        data.forEach(function (car) {
          var formattedSpeed = Math.floor(car.speed).toLocaleString("fr-FR");
          var formattedPrice = formatPrice(car.price);

          $("#cars ul").append(
            '<li class="car">' +
              "<div>" +
              '<img src="' +
              car.thumbnail +
              '" alt="">' +
              "</div>" +
              "<span>" +
              car.name +
              "</span>" +
              '<font size="2px">' +
              formattedSpeed +
              " KM | " +
              car.essence +
              "</font>" +
              '<span class="prix" id="price">' +
              formattedPrice +
              "€</span>" +
              '<a href="' +
              car.absolute_url +
              '">Voir</a>' +
              "</li>"
          );
        });
      },
      error: function (xhr, errmsg, err) {
        console.log(xhr.status + ": " + xhr.responseText);
      },
    });
  });
});

function formatPrice(price) {
  var formattedPrice = Math.floor(price).toLocaleString("fr-FR");
  return formattedPrice;
}
