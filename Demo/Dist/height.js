var select = document.getElementById("height")
    arr=["7", "8","9", "10" ,"11","12","13","14"]
    for(var i=0;i<arr.length;i++)
    {
        var option = document.createElement("OPTION"),
            txt=document.createTextNode(arr[i]);
            option.appendChild(txt);
            option.setAttribute("value",arr[i])
            select.insertBefore(option,select.lastChild);
    }
    function H(){
        var He=document.getElementById("height").value;
        console.log(He);
    }
