document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('macro-form');
    const result = document.getElementById('result');
    const generatedScript = document.getElementById('generated-script');
    const copyButton = document.getElementById('copy-button');
    const toggleGuidanceButton = document.getElementById('toggle-guidance');
    const guidanceContent = document.getElementById('guidance-content');

    toggleGuidanceButton.addEventListener('click', () => {
        guidanceContent.classList.toggle('hidden');
    });

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const filePath = document.getElementById('file-path').value;
        const macroAction = document.getElementById('macro-action').value;
        const macroType = document.getElementById('macro-type').value;

        try {
            const response = await fetch('/generate_script', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ filePath, macroAction, macroType }),
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const data = await response.json();
            generatedScript.textContent = data.script;
            result.classList.remove('hidden');
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred while generating the script. Please try again.');
        }
    });

    copyButton.addEventListener('click', () => {
        const scriptText = generatedScript.textContent;
        navigator.clipboard.writeText(scriptText).then(() => {
            alert('Script copied to clipboard!');
        }, (err) => {
            console.error('Could not copy text: ', err);
            alert('Failed to copy script. Please try selecting and copying manually.');
        });
    });
});
