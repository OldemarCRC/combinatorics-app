function hideResults() {
    document.getElementById('result-section').classList.remove('show');
    document.getElementById('error-section').style.display = 'none';
}

function showResult(data) {
    hideResults();
    document.getElementById('result-title').textContent = data.operation;
    document.getElementById('result-number').textContent = data.result.toLocaleString();

    if (data.formula) {
        document.getElementById('result-formula').textContent = data.formula;
        document.getElementById('result-formula').style.display = 'block';
    } else {
        document.getElementById('result-formula').style.display = 'none';
    }

    document.getElementById('result-section').classList.add('show');
}

function showError(message) {
    hideResults();
    document.getElementById('error-message').textContent = message;
    document.getElementById('error-section').style.display = 'block';
}

async function calculate(operation) {
    let data = { operation };

    try {
        if (operation === 'permutations') {
            data.n_items = parseInt(document.getElementById('perm-n').value);
            data.chosen_items = parseInt(document.getElementById('perm-r').value);
        } else if (operation === 'combinations') {
            data.n_items = parseInt(document.getElementById('comb-n').value);
            data.chosen_items = parseInt(document.getElementById('comb-r').value);
        } else if (operation === 'inversions') {
            data.permutation = document.getElementById('permutation').value.trim();
        }

        const response = await fetch('/calculate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (response.ok) {
            showResult(result);
        } else {
            showError(result.error);
        }
    } catch (error) {
        showError('Connection Error. Please try again.');
        console.error('Error:', error);
    }
}

// Permitir cálculo con Enter
document.addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        e.target.blur(); // Quitar foco del input
    }
});