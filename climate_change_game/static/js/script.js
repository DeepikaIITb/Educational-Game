const answers = [
    ["M", "", "", "", "", "", "", "", "", ""],
    ["E", "", "P", "", "", "", "", "", "", ""],
    ["T", "", "F", "", "", "", "", "", "", ""],
    ["H", "F", "C", "", "", "", "", "", "", ""],
    ["A", "", "O", "", "", "", "", "", "", ""],
    ["N", "", "2", "", "", "S", "", "", "", ""],
    ["E", "", "", "", "N", "F", "3", "", "", ""],
    ["", "", "", "", "2", "6", "", "", "", ""],
    ["", "", "", "", "O", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", ""]
];

function createGrid() {
    const grid = document.getElementById('grid');
    for (let i = 0; i < 10; i++) {
        for (let j = 0; j < 10; j++) {
            const cell = document.createElement('div');
            cell.className = 'cell';
            if (answers[i][j] !== "") {
                if (answers[i][j] === "H" || answers[i][j] === "N" || answers[i][j] === "6") {
                    cell.innerText = answers[i][j];
                    cell.classList.add('hint');
                } else {
                    cell.contentEditable = "true";
                }
            } else {
                cell.classList.add('blocked');
            }
            grid.appendChild(cell);
        }
    }
}

function checkAnswers() {
    const grid = document.getElementById('grid');
    let correct = true;
    for (let i = 0; i < 10; i++) {
        for (let j = 0; j < 10; j++) {
            const cell = grid.children[i * 10 + j];
            if (answers[i][j] !== "" && answers[i][j] !== "H" && answers[i][j] !== "N" && answers[i][j] !== "6" && cell.innerText !== answers[i][j]) {
                correct = false;
                break;
            }
        }
    }
    const message = document.getElementById('message');
    if (correct) {
        message.innerText = "Hurray! You got it right";
        document.getElementById('avatar-img').src = "/static/image/happy_avatar.jpg";
    } else {
        message.innerText = "Try again!";
        document.getElementById('avatar-img').src = "/static/image/sad_avatar.jpg";
    }
}

function showHint() {
    alert("Hint: Carbon Dioxide, Methane, Nitrous oxide, Hydrofluorocarbons, Perfluorocarbons, Sulphur hexafluoride, Nitrogen trifluoride. 'H', 'N', and '6' are already placed in their correct positions.");
}

function nextLevel() {
    const nextPuzzleId = 2; // Example: Assuming next puzzle ID is 2
    window.location.href = "/puzzle/" + nextPuzzleId;
}

createGrid();
