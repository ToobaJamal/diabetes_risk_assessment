function getnews() {
    fetch("https://newsapi.org/v2/top-headlines?q=health&apiKey=85a9eb6500e044739b0e3531e084b51b").
    then(res => res.json()).then(data =>  {
        const randomNews = Math.floor(Math.random() * data.articles.length)
        document.getElementById("news").style.backgroundImage = "url('"+data.articles[randomNews].urlToImage+"')"
        document.getElementById("news-title").innerHTML = data.articles[randomNews].title
        document.getElementById("news-link").href = data.articles[randomNews].url})
}
getnews()
setInterval(getnews, 20000)
