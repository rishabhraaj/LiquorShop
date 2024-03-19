function moveFocus(currentInput, nextInputIndex) {
    if (currentInput.value.length == 1) {
        document.getElementsByClassName('input-field')[0].children[nextInputIndex].focus();
    }
}

function moveFocusBack(currentInput, previousInputIndex) {
    if (event.key === 'Backspace' && currentInput.value.length === 0) {
        document.getElementsByClassName('input-field')[0].children[previousInputIndex].focus();
    }
}