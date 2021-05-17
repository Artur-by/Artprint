function getSumByColor(sum) {
    let color = document.getElementById('id_Цвет')
    if (color.value == 1){
        sum += 0
    }
    else if (color.value == 2){
        sum += 0.5
    }
    else if (color.value == 3){
        sum += 2
    }
    else if (color.value == 4){
        sum += 2
    }
    else if (color.value == 5){
        sum += 12
    }
    return sum
}

function getSumBySize(sum){
    let size = document.getElementById('id_Размер')
    if (size.value == 1){
        sum += 0
    }
    else{
        sum += 3
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
    sum = getSumBySize(sum)
    sum = getSumByPrint(sum)

    let output = document.getElementById('costValueText')
    output.innerHTML = sum + ' руб.'
}