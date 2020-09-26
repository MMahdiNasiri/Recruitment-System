 var currentTab = 0;
 var page = 0;
showTab(currentTab);

function showTab(n) {

  var x = document.getElementsByClassName("tab");
  x[n].style.display = "block";

  if (n == 0) {
    document.getElementById("prevBtn").style.display = "none";
  } else {
    document.getElementById("prevBtn").style.display = "inline";
  }
  if (n == (x.length - 1)) {
    document.getElementById("nextBtn").innerHTML = "Submit";
  } else {
    document.getElementById("nextBtn").innerHTML = "Next";
  }
  fixStepIndicator(n)
}

function nextPrev(n) {
  var x = document.getElementsByClassName("tab");
  console.log(x[currentTab]);
  if(n == 1){
    if (!validateForm(currentTab)) return false;
    saveForm(page);
  }
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
//    x = document.getElementsByClassName("tab");
//    y = x[currentTab].getElementsByTagName("input");

    if (currentTab == 0) {
        x = document.forms['myForm']['firstName'];
        y = x.getElementsByTagName("input");
        if (x.value == ''){
            y.className += " invalid";
            valid = false;
        }
        z = document.forms['myForm']['lastName'];
        v = z.getElementsByTagName("input");
        if (z.value == ''){
            v.className += " invalid";
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
            data = document.getElementById('form2');
            break;
        case 2:
            data = document.getElementById('form3');
            break;
    }

    request = new XMLHttpRequest();
    request.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            console.log(this.responseText);

       }
    };

    request.open('POST', 'save', true);
    const csrftoken = getCookie('csrftoken');
    request.setRequestHeader('X-CSRFToken', csrftoken);
    request.setRequestHeader('page', page)

//    request.setRequestHeader('Content-Type', 'application/json; charset=UTF-8');
//    request.setRequestHeader('X-Requested-With', 'XMLHttpRequest');

    request.send(data);
    return 0;
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
