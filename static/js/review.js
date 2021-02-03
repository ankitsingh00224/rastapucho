const alertBox = document.getElementById('alert-box')
const imageBox = document.getElementById('img')
const form = document.getElementById('ajax-form')

// console.log(form);
const name = document.getElementById('id_name')
const message = document.getElementById('id_message')
const image = document.getElementById('id_your_image')

const csrf = document.getElementsByName('csrfmiddlewaretoken')
// console.log(csrf);

// const img_url

image.addEventListener('change', () => {
  const img_data = image.files[0]
  const img_url = URL.createObjectURL(img_data)
  // console.log(url);
  imageBox.innerHTML = `<img src="${img_url}" width="100%" >`
})

// console.log(image.files[0]);


const handleAlerts = (type, text) =>{
    alertBox.innerHTML = `<div class="alert alert-${type}" role="alert">
                            ${text}
                        </div>`
}



form.addEventListener('submit', e=>{

  e.preventDefault()


  const form_data = new FormData()
  // const img_data = image.files[0]
  // const img_url = URL.createObjectURL(img_data)
  //
  // console.log(img_url);

  form_data.append('csrfmiddlewaretoken',csrf[0].value)
  form_data.append('name',name.value)
  form_data.append('message',message.value)
  form_data.append('image',image.files[0])

  // for (var key of form_data.entries()) {
  //       console.log(key[0] + ', ' + key[1]);
  //   }

  $.ajax({
    type: 'POST',
    url: '',
    enctype: 'multipart/form-data',
    data: form_data,
    success: function(response){
      const sText = `successfully saved ${response.name}`
        handleAlerts('success', sText)
        setTimeout(()=>{
            alertBox.innerHTML = ""
            imageBox.innerHTML = ""
            name.value = ""
            message.value = ""
            image.value = ""
        }, 3000)
    },
    error: function(error){
      handleAlerts('danger', 'oops..something went wrong')
    },
    cache: false,
    contentType: false,
    processData: false,
  })
})
