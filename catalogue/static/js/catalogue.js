$(document).ready( function () {

  console.log('catalogue.js')

  // init homepage carousel
  $('.carousel').carousel('cycle')

  // mialing-list form
  $('#mailing-list-form').submit(function(e){
    var form = $('#mailing-list-form')
      , formData = form.serializeArray()
      , postUrl = form.attr('action')
      , button = form.find('button')

    e.preventDefault()
    button.addClass('disabled')
    $.post(postUrl, formData, function(content, message, status){
        if (status.status === 200){
          $('input').val('')
          button.removeClass('btn-primary').addClass('btn-success').text('Success')
        } else {
          button.removeClass('disabled')
        }
    })
  })

})
