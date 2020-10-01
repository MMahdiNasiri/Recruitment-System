 var currentTab = 0;
 var page = 0;
 var defaultdata = {
    "firstName": document.getElementById('id_firstName').value,
    "lastName": document.getElementById('id_lastName').value,
    "birthPlace": document.getElementById('id_birthPlace').value,
    "gender": document.getElementById('id_gender').value,
    "phone_number": document.getElementById('id_phone_number').value,
    "email": document.getElementById('id_email').value,
    "province": document.getElementById('id_province').value,
    "city": document.getElementById('id_city').value,
    "address": document.getElementById('id_address').value,

    "education": document.getElementById('id_education').value,
    "field": document.getElementById('id_field').value,
    "university": document.getElementById('id_university').value,
    "studentNumber": document.getElementById('id_studentNumber').value,
    "religousEducation": document.getElementById('id_religousEducation').value,
    "englishLanguage": document.getElementById('id_englishLanguage').value,
    "arabicLanguage": document.getElementById('id_arabicLanguage').value,

    "fisically": document.getElementById('id_fisically').value,
    "defective": document.getElementById('id_defective').value,
    "disease": document.getElementById('id_disease').value,
    "drugs": document.getElementById('id_drugs').value
 }

showTab(currentTab);


function showTab(n) {
  var x = document.getElementsByClassName("tab");
  x[n].style.display = "block";

  if (n == 0) {
    document.getElementById("prevBtn").style.display = "none";
  } else {
    document.getElementById("prevBtn").style.display = "inline";
  }
//  if (n == (x.length - 1)) {
//    document.getElementById("nextBtn").innerHTML = "Submit";
//  } else {
//    document.getElementById("nextBtn").innerHTML = "Next";
//  }
  fixStepIndicator(n)
}

function nextPrev(n) {
  var x = document.getElementsByClassName("tab");
  if (page == 3){
        location.replace("../done/")
  }
  console.log(x[currentTab]);
  if(n == 1){
    if (!validateForm(currentTab)) return false;
  }
  saveForm(page);
  x[currentTab].style.display = "none";
  currentTab = currentTab + n;

  page = page + n;

  if (currentTab >= x.length) {
    document.getElementById("regForm").submit();
    return false;
  }
  showTab(currentTab);
}

function validateForm(currentTab) {
    var x, y, z, v,valid = true;

    if (currentTab == 0) {
        var phoneregex = /^\0?1?\d{10,11}$/
        var nameregex = /\[A-z]/gi
        var emailregex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;

        x = document.forms['myForm']['firstName'];
        y = x.getElementsByTagName("input");
        if (x.value == '' || nameregex.test(x.value) ){
            y.className += " invalid";
            valid = false;
        }
        x = document.forms['myForm']['lastName'];
        y = x.getElementsByTagName("input");
        if (x.value == ''|| nameregex.test(x.value)){
            y.className += " invalid";
            valid = false;
        }
        x = document.forms['myForm']['phone_number'];
        y = x.getElementsByTagName("input");
        if (x.value != '' && phoneregex.test(x.value)){
            y.className += " invalid";
            valid = false;
        }
        x = document.forms['myForm']['email'];
        y = x.getElementsByTagName("input");
        if (x.value != '' && emailregex.test(x.value)){
            y.className += " invalid";
            valid = false;
        }
        x = document.forms['myForm']['province'];
        y = x.getElementsByTagName("input");
        if (x.value != '' && nameregex.test(x.value)){
            y.className += " invalid";
            valid = false;
        }
        x = document.forms['myForm']['city'];
        y = x.getElementsByTagName("input");
        if (x.value != '' && nameregex.test(x.value)){
            y.className += " invalid";
            valid = false;
        }
    }
    if (valid) {
    document.getElementsByClassName("step")[currentTab].className += " finish";
    }
    return valid;
}

function fixStepIndicator(n) {
  var i, x = document.getElementsByClassName("step");
  for (i = 0; i < x.length; i++) {
    x[i].className = x[i].className.replace(" active", "");
  }
  x[n].className += " active";
}

function saveForm(page){
    switch(page){
        case 0:
            firstName = document.getElementById('id_firstName').value;
            lastName = document.getElementById('id_lastName').value;
            birthPlace = document.getElementById('id_birthPlace').value;
            gender = document.getElementById('id_gender').value;
            phone_number = document.getElementById('id_phone_number').value;
            email = document.getElementById('id_email').value;
            province = document.getElementById('id_province').value;
            city = document.getElementById('id_city').value;
            address = document.getElementById('id_address').value;
            data = {
                "firstName": firstName,
                "lastName": lastName,
                "birthPlace": birthPlace,
                "gender": gender,
                "phone_number": phone_number,
                "email": email,
                "province": province,
                "city": city,
                "address": address
            }
            break;
        case 1:
            education = document.getElementById('id_education').value;
            field = document.getElementById('id_field').value;
            university = document.getElementById('id_university').value;
            studentNumber = document.getElementById('id_studentNumber').value;
            religousEducation = document.getElementById('id_religousEducation').value;
            englishLanguage = document.getElementById('id_englishLanguage').value;
            arabicLanguage = document.getElementById('id_arabicLanguage').value;
            data = {
                "education": education,
                "field": field,
                "university": university,
                "studentNumber": studentNumber,
                "religousEducation": religousEducation,
                "englishLanguage": englishLanguage,
                "arabicLanguage": arabicLanguage
            }
            break;
        case 2:
            fisically = document.getElementById('id_fisically').value;
            defective = document.getElementById('id_defective').value;
            disease = document.getElementById('id_disease').value;
            drugs = document.getElementById('id_drugs').value;
            data = {
                "fisically": fisically,
                "defective": defective,
                "disease": disease,
                "drugs": drugs
            }
            break;
    }
    if (checkDirty(data, page) || page == 2){
        console.log('pass the check dirty')
        const csrftoken = getCookie('csrftoken');
        fetch('save', {
          method: "POST",
          body: JSON.stringify(data),
          headers: {"Content-type": "application/json; charset=UTF-8",
                    'X-CSRFToken': csrftoken,
                    'page': page
          }
        })
        .then(response => response.json())
        .then(json => console.log(json));
    }
    return 0;
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function checkDirty(data, page){
    if (page == 0 ){
        if(defaultdata.firstName == data.firstName
            && defaultdata.lastName == data.lastName
            && defaultdata.birthPlace == data.birthPlace
            && defaultdata.gender == data.gender
            && defaultdata.phone_number == data.phone_number
            && defaultdata.email == data.email
            && defaultdata.province == data.province
            && defaultdata.city == data.city
            && defaultdata.address == data.address){
                return false;
             }else{
                defaultdata.firstName = data.firstName;
                defaultdata.lastName = data.lastName;
                defaultdata.birthPlace = data.birthPlace;
                defaultdata.gender = data.gender;
                defaultdata.phone_number = data.phone_number;
                defaultdata.email = data.email;
                defaultdata.province = data.province;
                defaultdata.city = data.city;
                defaultdata.address = data.address;
                return true;
             }
    }else if(page == 1){
        console.log('check dirty 1')
        if (defaultdata.education == data.education
             && defaultdata.field == data.field
             && defaultdata.university == data.university
             && defaultdata.studentNumber == data.studentNumber
             && defaultdata.religousEducation == data.religousEducation
             && defaultdata.englishLanguage == data.englishLanguage
             && defaultdata.arabicLanguage == data.arabicLanguage){
                return false;
             }else{
                 defaultdata.education = data.education;
                 defaultdata.field = data.field;
                 defaultdata.university = data.university;
                 defaultdata.studentNumber = data.studentNumber;
                 defaultdata.religousEducation = data.religousEducation;
                 defaultdata.englishLanguage = data.englishLanguage;
                 defaultdata.arabicLanguage = data.arabicLanguage;
                 return true;
             }
    }else if (page == 2){
        if(defaultdata.fisically == data.fisically
            && defaultdata.defective == data.defective
            && defaultdata.disease == data.disease
            && defaultdata.drugs == data.drugs
        ){
            return false;
        }else{
            defaultdata.fisically = data.fisically;
            defaultdata.defective = data.defective;
            defaultdata.disease = data.disease;
            defaultdata.drugs = data.drugs;
            return true;
        }
    }

}
