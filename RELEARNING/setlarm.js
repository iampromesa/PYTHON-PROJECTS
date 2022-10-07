function setAlarm (employed, vacation) {
    let result;
    switch (true) {
      case (employed == true && vacation == true):
      case (employed == false && vacation == true):
      case (employed == false && vacation == false):
        result = false;
        break;
  
      default:
        result = true;
        break;
    }
  
    console.log(result);
  }
  
  setAlarm(false, true);