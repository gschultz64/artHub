$('document').ready(function() {

});

// Cloudinary Blueimp File Upload library
$(function () {
  if ($.fn.cloudinary_fileupload !== undefined) {
    $("input.cloudinary-fileupload[type=file]").cloudinary_fileupload();
  }
});

// Cloudinary upload progress and done notifications
$('.cloudinary-fileupload').bind('cloudinarydone', function (e, data) {
  $('.preview').html(
    $.cloudinary.image(data.result.public_id,
      {
        format: data.result.format, version: data.result.version,
        crop: 'fill', width: 150, height: 100
      })
  );
  $('.image_public_id').val(data.result.public_id);
  return true;
});
$('.cloudinary-fileupload').bind('fileuploadprogress', function (e, data) {
  $('.progress_bar').css('width', Math.round((data.loaded * 100.0) / data.total) + '%');
});