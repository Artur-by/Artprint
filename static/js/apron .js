function getSumByCant(sum) {
    let cant = document.getElementById('id_Кант')
    if (cant.value == 1){
        sum += 0
    }
    else if (cant.value == 2){
        sum += 0.5
    }
    return sum
}


function getSumByPrint(sum) {
    let format = document.getElementById('id_Формат')
    if (format.value == 1){
        sum += 1
    }
    else if (format.value == 2){
        sum += 2
    }
    else {
        sum += 3
    }
    return sum
}

function costValue(){
    let sum = 7
    sum = getSumByCant(sum)
    sum = getSumByPrint(sum)

    let output = document.getElementById('costValueText')
    output.innerHTML = ' Цена '+ sum + ' руб.'
}