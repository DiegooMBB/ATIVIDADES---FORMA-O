var notas=[]
var n1 = parseFloat(prompt("Qual a sua primeira nota? "));
notas.push(n1)
var n2 = parseFloat(prompt("Qual a sua segunda nota? "));
notas.push(n2)
var n3 = parseFloat(prompt("Qual a sua terceira nota? "));
notas.push(n3)
function soma(arr) {
    var total = 0;
    for (var i = 0; i < arr.length; i++) {
      total += arr[i];
    }
    return total;
  }
var media = soma(notas)/3;
if (media<=4) {
    alert("O aluno está reprovado.") 
} else if (media > 4 && media < 7){
    let recup = parseFloat(prompt("Aluno foi para recuperacao. Qual a sua nota na recuperacao? "));
    let mediaf=(media + recup)/2
    if (mediaf>=5) {
        alert("O aluno esta aprovado.")
    } else {
        alert("O aluno esta reprovado")
    }
}else{
    alert("O aluno está aprovado.")
}4