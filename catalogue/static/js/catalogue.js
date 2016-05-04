$(document).ready( function () {

  // init homepage carousel
  $('.carousel').carousel('cycle')

  // mailing-list form
  $('#mailing-list-form').submit(function(e){

    var form = $('#mailing-list-form')
      , formData = form.serializeArray()
      , postUrl = form.attr('action')
      , button = form.find('button')
      , helpBlock = $('.help-block')

    e.preventDefault()
    button.addClass('disabled')
    
    // ajax post data
    $.post(postUrl, formData, function(content, message, status){
      if (content.message === 'failed'){
        helpBlock.text(content.email[0])
        form.addClass('has-error')
        button.removeClass('disabled')
      } else {
        $('input').val('')
        button.removeClass('btn-primary').addClass('btn-success').text('Success')
        form.removeClass('has-error')
        helpBlock.text(content.message)
      }
      helpBlock.removeClass('hidden')
    })
  })

})
