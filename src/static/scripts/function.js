
document.getElementById('copy').addEventListener('click',()=>{
	Copy(document.getElementById('copy'))
})


function Copy(element){
    navigator.clipboard.writeText(element.value).then(()=>{})
}