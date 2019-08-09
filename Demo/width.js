var select = document.getElementById("width")
    arr=["21", "26","31", "36" ,"41"]
    for(var i=0;i<arr.length;i++)
    {
        var option = document.createElement("OPTION"),
            txt=document.createTextNode(arr[i]);
            option.appendChild(txt);
            option.setAttribute("value",arr[i])
            select.insertBefore(option,select.lastChild);
    }
    function Wi(){
        var W=document.getElementById("width").value;
        console.log(W);
    }
