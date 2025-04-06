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
      // Make an AJAX GET request to delete the item
      $.ajax({
        url: "/delete/" + id + "/", // Ensure that the URL matches your Django setup
        type: "GET", // Using GET method for deletion
        success: function () {
          // Redirect to wishlist upon successful deletion
          window.location.href = "/wishlist/";
        },
        error: function (xhr, status, error) {
          // Log any errors and alert the user
          console.error("AJAX Error:", status, error);
          Swal.fire("خطأ!", "فشل حذف العنصر: " + error, "error");
        },
      });
    }
  });
};
