document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('prediction-form');
    const resultContainer = document.getElementById('result-container');
    const submitBtn = document.getElementById('submit-btn');
    const btnText = submitBtn.querySelector('.btn-text');
    const loader = document.getElementById('loader');
    const statusBadge = document.getElementById('status-badge');
    const confidenceScore = document.getElementById('confidence-score');
    const resetBtn = document.getElementById('reset-btn');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        // Show loading state
        btnText.style.display = 'none';
        loader.style.display = 'block';
        submitBtn.disabled = true;
        
        // Gather data
        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());
        
        // Convert to numbers
        Object.keys(data).forEach(key => {
            data[key] = Number(data[key]);
        });

        try {
            const response = await fetch('/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            });

            if (!response.ok) {
                throw new Error('Prediction request failed');
            }

            const result = await response.json();
            
            // Display result
            displayResult(result);
            
            // Hide form, show result
            form.closest('.card').classList.add('hidden');
            resultContainer.classList.remove('hidden');

        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred while assessing the risk. Please try again.');
        } finally {
            // Restore button state
            btnText.style.display = 'block';
            loader.style.display = 'none';
            submitBtn.disabled = false;
        }
    });

    resetBtn.addEventListener('click', () => {
        form.reset();
        resultContainer.classList.add('hidden');
        form.closest('.card').classList.remove('hidden');
    });

    function displayResult(result) {
        statusBadge.textContent = result.status;
        statusBadge.className = 'status-badge ' + (result.status === 'Approved' ? 'status-approved' : 'status-rejected');
        
        const confidencePercent = (result.confidence * 100).toFixed(1);
        confidenceScore.textContent = `${confidencePercent}%`;
    }
});
