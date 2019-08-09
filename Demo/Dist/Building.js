var select = document.getElementById("building") ,
    arr=["Barns", "Carports", "Combo Unit","Garage", "RV Covers", "Sheds"];

for(var i=0;i<arr.length;i++)
{
    var option = document.createElement("OPTION"),
        txt=document.createTextNode(arr[i]);
    option.appendChild(txt);
    option.setAttribute("value",arr[i])
    select.insertBefore(option,select.lastChild);
}

function buildT(){
    var built=document.getElementById("building").value;
    console.log(built);
}
