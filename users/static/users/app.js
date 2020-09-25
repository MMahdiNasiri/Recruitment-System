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
    saveForm(page)
    console.log('in this shit')
  }
  console.log('out of if')
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
            myForm = document.getElementById('form1');
            break;
        case 1:
            myForm = document.getElementById('form2');
            break;
        case 2:
            myForm = document.getElementById('form3');
            break;
    }

    request = new XMLHttpRequest();

    request.open('POST', '', true);
    request.setRequestHeader('csrfmiddlewaretoken', '{% csrf_token %}');
//    request.setRequestHeader('Content-Type', 'application/json; charset=UTF-8');
//    request.setRequestHeader('X-Requested-With', 'XMLHttpRequest');

    request.send(myForm);
    return 0;
}