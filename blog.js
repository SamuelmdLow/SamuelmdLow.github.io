var blog = [["<img src=\"images/icon.jpg\">","<text>epic pee and poo and also farting I love farting I' quite a fast typer I yhik Im pretyy fasy like damn look at my I'm so dawmn fast yeahhhh baby lets go look how fast a typer I am</text>"], ["<img src=\"images/icon.jpg\">","<text>pee</text>"]];
var article = ""

for (i=0; i<blog.length; i++)
{
    article = article + "<tr>";
    for (a=0; a<blog[i].length; a++)
    {
        article = article + "<td>" +blog[i][a] + "</td>";
    }
    article = article + "</tr>";
}

document.getElementById("blog").innerHTML = article;