var select = document.getElementById("select") ,
    arr=["Arizona", "Colorado","Kansas","New Mexico","Texas"];

for(var i=0;i<arr.length;i++)
{
    var option = document.createElement("OPTION"),
        txt=document.createTextNode(arr[i]);
    option.appendChild(txt);
    option.setAttribute("value",arr[i])
    select.insertBefore(option,select.lastChild);
}
