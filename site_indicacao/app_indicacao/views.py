from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from app_indicacao.forms import LeadForm
import requests
import base64
import json
from app_indicacao.constantes import TOKEN, IPSERVIDOR
from app_indicacao.models import Cupom, Leads

def index(request):
    leads = LeadForm()
    contexto = {
        'leads':leads,
    }
    return render(request, 'index.html', contexto)

def enviaDados(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            contexto = {
                'form':form,
            }
            
            envia_dados_api(form)

            salva_lead_bd(request)

    return render(request, 'confirma.html', contexto) 

def salva_lead_bd(request):
    nome = request.POST['nome']
    fone_celular = request.POST['fone_celular']
    fone_whatsapp = request.POST['fone_whatsapp']
    email = request.POST['email']
    cidade = request.POST['cidade']
    uf = request.POST['uf']
    obs = request.POST['obs']  
    cupon = get_object_or_404(Cupom, pk=request.POST['cupon'])
    lead = Leads.objects.create(nome = nome, fone_celular=fone_celular, fone_whatsapp=fone_whatsapp,
            email=email, cidade=cidade, uf=uf, obs=obs, cupon=cupon,)
    lead.save()

def envia_dados_api(form):
    host = IPSERVIDOR
    url = "https://{}/webservice/v1/contato".format(host)
    token = TOKEN.encode('utf-8')

    payload = json.dumps({
                'principal': 'N',
                'id_cliente': '',
                'nome': f'{form.cleaned_data.get("nome")}',
                'tipo_pessoa': 'F',
                'cnpj_cpf': '',
                'data_nascimento': '',
                'razao': '',
                'id_filial': '',
                'id_contato_tipo': '',
                'id_candidato_tipo': '',
                'id_responsavel': '',
                'data_cadastro': f'{form.cleaned_data.get("data_cadastro")}',
                'data': '',
                'id_vd_contrato': '',
                'id_tipo_elemento': '',
                'velocidade_calculada': '',
                'id_fornecedor': '',
                'lead': 'S',
                'ativo': 'S',
                'id_caixa_ftth': '',
                'distancia_caixa_mais_proxima': '',
                'id_prospeccao': '',
                'ultima_atualizacao': 'CURRENT_TIMESTAMP',
                'fone_residencial': '',
                'fone_comercial': '',
                'fone_celular': f'{form.cleaned_data.get("fone_celular")}',
                'fone_whatsapp': f'{form.cleaned_data.get("fone_whatsapp")}',
                'email': f'{form.cleaned_data.get("email")}',
                'skype': '',
                'facebook': '',
                'website': '',
                'cep': '',
                'endereco': '',
                'numero': '',
                'bairro': '',
                'complemento': '',
                'cidade': '',
                'uf': '',
                'referencia': '',
                'latitude': '',
                'longitude': '',
                'pipe_id_pessoa': '',
                'cadastro_site': 'N',
                'status_viabilidade': '',
                'data_ult_verificacao_viab': '',
                'caixa_mais_proxima': '',
                'data_cadastro_lead': '',
                'velocidade_calculada_lead': '',
                'quantidade_pessoas_lead': '',
                'quantidade_smart_lead': '',
                'frequencia_smart_lead': '',
                'quantidade_celular_lead': '',
                'frequencia_celular_lead': '',
                'quantidade_computador_lead': '',
                'frequencia_computador_lead': '',
                'quantidade_console_lead': '',
                'frequencia_console_lead': '',
                'obs': '',
                'alerta': ''
            })

    headers = {
                'ixcsoft': '',
                'Authorization': 'Basic {}'.format(base64.b64encode(token).decode('utf-8')),
                'Content-Type': 'application/json'
            }

    response = requests.post(url, data=payload, headers=headers, verify=False)

    print(response.text)     

# Create your views here.
