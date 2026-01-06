const searchInput = document.getElementById('searchInput');
const resultsDiv = document.getElementById('results');
const loadingDiv = document.getElementById('loading');

let debounceTimer;

searchInput.addEventListener('input', (e) => {
    clearTimeout(debounceTimer);
    const query = e.target.value.trim();

    if (query.length === 0) {
        resultsDiv.innerHTML = '';
        return;
    }

    debounceTimer = setTimeout(() => {
        performSearch(query);
    }, 300);
});

async function performSearch(query) {
    loadingDiv.classList.remove('hidden');
    resultsDiv.innerHTML = '';

    try {
        const res = await fetch(`/api/search?q=${encodeURIComponent(query)}`);
        const data = await res.json();

        loadingDiv.classList.add('hidden');
        renderResults(data);
    } catch (err) {
        console.error(err);
        loadingDiv.textContent = 'Error occurred';
    }
}

function renderResults(results) {
    if (results.length === 0) {
        resultsDiv.innerHTML = '<div style="text-align:center; color: #94a3b8;">No results found</div>';
        return;
    }

    resultsDiv.innerHTML = results.map(item => `
        <div class="result-card" onclick="openFile('${item.path.replace(/\\/g, '\\\\')}')">
            <span class="file-path">${item.path}</span>
            <div class="file-name">${item.file_name}</div>
            <div class="snippet">${escapeHtml(item.snippet)}</div>
        </div>
    `).join('');
}

async function openFile(path) {
    try {
        await fetch('/api/open', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ path: path }),
        });
    } catch (err) {
        console.error('Error opening file:', err);
    }
}

function escapeHtml(text) {
    return text
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
}
