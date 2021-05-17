function getSumByColor(sum) {
    let color = document.getElementById('id_Цвет')
    if (color.value == 1){
        sum += 0
    }
    else if (color.value == 2){
        sum += 0.5
    }
    else if (color.value == 3){
        sum += 0
    }

    return sum
}


function getSumByPrint(sum) {
    let format = document.getElementById('id_Формат')
    if (format.value == 1){
        sum += 5
    }
    else {
        sum += 7
    }
    return sum
}

function costValue(){
    let sum = 6
    sum = getSumByColor(sum)
    sum = getSumByPrint(sum)

    let output = document.getElementById('costValueText')
    output.innerHTML = sum + ' руб.'
}

function zamena(){
    let a = document.getElementById('id')
    if(a == "img1") img1.src="{% static 'min/shop2.jpg' %}";
    return false;
}


