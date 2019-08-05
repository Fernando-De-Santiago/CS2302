var select = document.getElementById("roofs")
    arr=["12, 21 7","12, 21 8","Vertical"]
    for(var i=0;i<arr.length;i++)
    {
        var option = document.createElement("OPTION"),
            txt=document.createTextNode(arr[i]);
            option.appendChild(txt);
            option.setAttribute("value",arr[i])
            select.insertBefore(option,select.lastChild);
    }
