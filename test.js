fetch('https://api.writesonic.com/v1/botsonic/botsonic/generate/656bdad6-5adf-48d3-b124-5f68c8db6fae', {
    method: 'POST',
    headers: {
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'User-Agent': 'python-requests/2.28.1',
        'accept': 'application/json',
        'token': '8dd725e8-48ee-42c3-b594-5b316124b018'
    },
    // body: '{"question": "How to develop these skills?", "chat_history": []}',
    body: JSON.stringify({
        'question': 'How to develop these skills?',
        'chat_history': []
    })
});