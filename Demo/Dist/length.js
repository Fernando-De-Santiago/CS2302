var select = document.getElementById("length")
    arr=["12", "18","20", "22" ,"24"]
    for(var i=0;i<arr.length;i++)
    {
        var option = document.createElement("OPTION"),
            txt=document.createTextNode(arr[i]);
            option.appendChild(txt);
            option.setAttribute("value",arr[i])
            select.insertBefore(option,select.lastChild);
    }
    function L(){
        var Le=document.getElementById("length").value;
        console.log(Le);
    }
