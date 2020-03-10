def crearVotante(request):
    if request.method == 'POST':
        votante_form = VotanteForm(request.POST)
        if votante_form.is_valid():
            votante_form.save()
            return redirect('index')
    else:
        votante_form = VotanteForm()
    return render(request,'crearv.html',{'votante_form':votante_form})

def listarVotante(request):
    votantes = Votante.objects.filter(estado = True)
    return render(request,'listadov.html',{'votantes':votantes})

def editarVotante(request,id):
    votante_form = None
    error = None
    try:
        votante = Votante.objects.get(id = id)
        if request.method == 'GET':
            votante_form = VotanteForm(instance = votante)
        else:
            votante_form = VotanteForm(request.POST, instance = votante)
            if votante_form.is_valid():
                votante_form.save()
            return redirect('listadov')
    except ObjectDoesNotExist as e:
        error = e
    return render(request,'listadov.html',{'votante_form':votante_form,'error':error})

def eliminarVotante(request,id):
    votante = Votante.objects.get(id = id)
    votante.estado = False
    votante.save()
    return redirect('listadov')
