def crearCandidato(request):
    if request.method == 'POST':
        candidato_form = CandidatoForm(request.POST)
        if candidato_form.is_valid():
            candidato_form.save()
            return redirect('index')
    else:
        candidato_form = CandidatoForm()
    return render(request,'lista/crear_candidato.html',{'candidato_form':candidato_form})

def listarCandidato(request):
    candidatos = Candidato.objects.filter(estado = True)
    return render(request,'lista/listar_candidato.html',{'candidatos':candidatos})

def editarCandidato(request,id):
    candidato_form = None
    error = None
    try:
        candidato = Candidato.objects.get(id = id)
        if request.method == 'GET':
            candidato_form = CandidatoForm(instance = candidato)
        else:
            candidato_form = CandidatoForm(request.POST, instance = candidato)
            if candidato_form.is_valid():
                candidato_form.save()
            return redirect('lista:listar_candidato')
    except ObjectDoesNotExist as e:
        error = e
    return render(request,'lista/crear_candidato.html',{'candidato_form':candidato_form,'error':error})

def eliminarCandidato(request,id):
    candidato = Candidato.objects.get(id = id)
    candidato.estado = False
    candidato.save()
    return redirect('lista:listar_candidato')
