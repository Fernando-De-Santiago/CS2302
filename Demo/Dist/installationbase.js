var select = document.getElementById("selects") ,
    arr=["Asphalt","Concrete","Ground"];//might need to add more or remove more

for(var i=0;i<arr.length;i++)
{
    var option = document.createElement("OPTION"),
        txt=document.createTextNode(arr[i]);
    option.appendChild(txt);
    option.setAttribute("value",arr[i])
    select.insertBefore(option,select.lastChild);
}
