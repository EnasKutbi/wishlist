let deleteItem = (id) => {
  Swal.fire({
    title: "هل أنت متأكد؟",
    text: "لن تتمكن من استرجاع هذا العنصر بعد الحذف!",
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#d33",
    cancelButtonColor: "#3085d6",
    confirmButtonText: "نعم، احذف!",
    cancelButtonText: "إلغاء",
  }).then((result) => {
    if (result.isConfirmed) {
      $.ajax({
        url: "/delete/" + id ,
        type: "GET", 
        success: function () {
          window.location.href = "/wishlist/";
        },
        error: function (xhr, status, error) {
          console.error("AJAX Error:", status, error);
          Swal.fire("خطأ!", "فشل حذف العنصر: " + error, "error");
        },
      });
    }
  });
};

function addCart() {
  $.ajax({
    url: "/addtocart/",
    type: "get",

    success: function (result) {
      // console.log(result.cart_count)
      $(".cart-count").text(result.cart_count);
    },
  });
}
