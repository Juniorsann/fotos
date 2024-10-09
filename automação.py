from PIL import Image, ImageDraw, ImageFont
import os

modelos_por_pasta = {
    "Campina Grande/Empreendedor Aprendiz": {
        "modelo": "EMPREENDEDOR APRENDIZ.png",
        "output": "AVD24.1/campina_grande/empreendedor_aprendiz/"
    },
    "Campina Grande/Empreendedor Potencial": {
        "modelo": "EMPREENDEDOR EM POTENCIAL.png",
        "output": "AVD24.1/campina_grande/empreendedor_potencial/"
    },
    "Campina Grande/Empreendedor em Ascenção": {  
        "modelo": "EMPREENDEDOR EM ASCENSÃO.png",
        "output": "AVD24.1/campina_grande/empreendedor_ascensao/"
    },
    "Litoral Norte/Empreendedor em Ascenção": {  
        "modelo": "EMPREENDEDOR EM ASCENSÃO.png",
        "output": "AVD24.1/litoral_norte/empreendedor_ascensao/"
    },
    "Litoral Norte/Empreendedor Potencial": {  
        "modelo": "EMPREENDEDOR EM POTENCIAL.png",
        "output": "AVD24.1/litoral_norte/empreendedor_potencial/"
    },
    "Litoral Norte/Empreendedor Aprendiz": {  
        "modelo": "EMPREENDEDOR APRENDIZ.png",
        "output": "AVD24.1/litoral_norte/empreendedor_aprendiz/"
    },
    "Mossoró/Empreendedor Aprendiz": {  
        "modelo": "EMPREENDEDOR APRENDIZ.png",
        "output": "AVD24.1/mossoro/empreendedor_aprendiz/"
    },
    "Mossoró/Empreendedor Potencial": {  
        "modelo": "EMPREENDEDOR EM POTENCIAL.png",
        "output": "AVD24.1/mossoro/empreendedor_potencial/"
    },
    "Mossoró/Empreendedor em Ascensão": {  
        "modelo": "EMPREENDEDOR EM ASCENSÃO.png",
        "output": "AVD24.1/mossoro/empreendedor_ascensão/"
    },
    "Leste da Paraíba/Empreendedor Aprendiz": {  
        "modelo": "EMPREENDEDOR EM ASCENSÃO.png",
        "output": "AVD24.1/leste_paraiba/empreendedor_aprendiz/"
    },
    "Leste da Paraíba/Empreendedor Potencial": {  
        "modelo": "EMPREENDEDOR EM POTENCIAL.png",
        "output": "AVD24.1/leste_paraiba/empreendedor_potencial/"
    },
    "OCE/Empreendedor Potencial": {  
        "modelo": "EMPREENDEDOR EM POTENCIAL.png",
        "output": "AVD24.1/oce/empreendedor_potencial/"
    },
    "OCE/Empreendedor em Ascenção": {  
        "modelo": "EMPREENDEDOR EM ASCENSÃO.png",
        "output": "AVD24.1/oce/empreendedor_ascensão/"
    },
    "OCE/Empreendedor Aprendiz": {  
        "modelo": "EMPREENDEDOR APRENDIZ.png",
        "output": "AVD24.1/oce/empreendedor_aprendiz/"
    },
    "Oeste do Maranhão/Empreendedor Aprendiz": {  
        "modelo": "EMPREENDEDOR APRENDIZ.png",
        "output": "AVD24.1/oma/empreendedor_aprendiz/"
    },
    "Oeste do Maranhão/Empreendedor Potencial": {  
        "modelo": "EMPREENDEDOR EM POTENCIAL.png",
        "output": "AVD24.1/oma/empreendedor_potencial/"
    },
    "Oeste do Maranhão/Empreendedor em Ascenção": {  
        "modelo": "EMPREENDEDOR EM ASCENSÃO.png",
        "output": "AVD24.1/oma/empreendedor_ascensão/"
    },
    "Retaguarda/Contabilidade/Empreendedor Aprendiz": {  
        "modelo": "EMPREENDEDOR APRENDIZ.png",
        "output": "AVD24.1/retaguarda/contabilidade/empreendedor_aprendiz"
    },
    "Retaguarda/Departamento Pessoal/Empreendedor Aprendiz": {  
        "modelo": "EMPREENDEDOR APRENDIZ.png",
        "output": "AVD24.1/retaguarda/contabilidade/empreendedor_aprendiz"
    },
    "Retaguarda/Departamento Pessoal/Empreendedor em Ascenção": {  
        "modelo": "EMPREENDEDOR EM ASCENSÃO.png",
        "output": "AVD24.1/retaguarda/departamento_pessoal/empreendedor_ascensão"
    },
    "Retaguarda/Departamento Pessoal/Empreendedor Potencial": {  
        "modelo": "EMPREENDEDOR EM POTENCIAL.png",
        "output": "AVD24.1/retaguarda/departamento_pessoal/empreendedor_potencial"
    },
    "Retaguarda/Financeiro/Empreendedor Potencial": {  
        "modelo": "EMPREENDEDOR EM POTENCIAL.png",
        "output": "AVD24.1/retaguarda/financeiro/empreendedor_potencial"
    },
    "Retaguarda/Financeiro/Empreendedor Aprendiz": {  
        "modelo": "EMPREENDEDOR APRENDIZ.png",
        "output": "AVD24.1/retaguarda/financeiro/empreendedor_aprendiz"
    },
    "Retaguarda/Gente e Cultura/Empreendedor Aprendiz": {  
        "modelo": "EMPREENDEDOR APRENDIZ.png",
        "output": "AVD24.1/retaguarda/gente_e_cultura/empreendedor_aprendiz"
    },
    "Retaguarda/IAF/Empreendedor em Ascenção": {  
        "modelo": "EMPREENDEDOR EM ASCENSÃO.png",
        "output": "AVD24.1/retaguarda/iaf/empreendedor_ascensão"
    },
    "Retaguarda/Júridico/Empreendedor Potencial": {  
        "modelo": "EMPREENDEDOR EM POTENCIAL.png",
        "output": "AVD24.1/retaguarda/jurídico/empreendedor_potencial"
    },
    "Retaguarda/Marketing/Empreendedor Potencial": {  
        "modelo": "EMPREENDEDOR EM POTENCIAL.png",
        "output": "AVD24.1/retaguarda/marketing/empreendedor_potencial"
    },
    "Retaguarda/Marketing/Empreendedor Aprendiz": {  
        "modelo": "EMPREENDEDOR APRENDIZ.png",
        "output": "AVD24.1/retaguarda/marketing/empreendedor_aprendiz"
    },
    "Retaguarda/Núcleo de Excelência/Empreendedor Aprendiz": {  
        "modelo": "EMPREENDEDOR APRENDIZ.png",
        "output": "AVD24.1/retaguarda/nex/empreendedor_aprendiz"
    },
    "Retaguarda/Núcleo de Excelência/Empreendedor Potencial": {  
        "modelo": "EMPREENDEDOR EM POTENCIAL.png",
        "output": "AVD24.1/retaguarda/nex/empreendedor_potencial"
    },
    "Retaguarda/Núcleo de Excelência/Empreendedor em Ascenção": {  
        "modelo": "EMPREENDEDOR EM ASCENÇÃO.png",
        "output": "AVD24.1/retaguarda/nex/empreendedor_ascensão"
    },
    "Retaguarda/Segurança/Empreendedor em Ascenção": {  
        "modelo": "EMPREENDEDOR EM ASCENÇÃO.png",
        "output": "AVD24.1/retaguarda/segurança/empreendedor_ascensão"
    },
    "Retaguarda/Segurança/Empreendedor Potencial": {  
        "modelo": "EMPREENDEDOR EM POTENCIAL.png",
        "output": "AVD24.1/retaguarda/segurança/empreendedor_potencial"
    },
    "Retaguarda/Segurança/Empreendedor Aprendiz": {  
        "modelo": "EMPREENDEDOR APRENDIZ.png",
        "output": "AVD24.1/retaguarda/segurança/empreendedor_aprendiz"
    },
    "Retaguarda/Suprimentos Diretos/Empreendedor Aprendiz": {  
        "modelo": "EMPREENDEDOR APRENDIZ.png",
        "output": "AVD24.1/retaguarda/suprimentos_diretos/empreendedor_aprendiz"
    },
    "Retaguarda/Suprimentos Diretos/Empreendedor Potencial": {  
        "modelo": "EMPREENDEDOR EM POTENCIAL.png",
        "output": "AVD24.1/retaguarda/suprimentos_diretos/empreendedor_potencial"
    },
    "Retaguarda/Suprimentos Estoque/Empreendedor Potencial": {  
        "modelo": "EMPREENDEDOR EM POTENCIAL.png",
        "output": "AVD24.1/retaguarda/suprimentos_estoque/empreendedor_potencial"
    },
    "Retaguarda/Suprimentos Estoque/Empreendedor Aprendiz": {  
        "modelo": "EMPREENDEDOR APRENDIZ.png",
        "output": "AVD24.1/retaguarda/suprimentos_estoque/empreendedor_aprendiz"
    },
    "Retaguarda/Suprimentos Estoque/Empreendedor em Ascenção": {  
        "modelo": "EMPREENDEDOR EM ASCENSÃO.png",
        "output": "AVD24.1/retaguarda/suprimentos_estoque/empreendedor_ascensão"
    },
    "Retaguarda/Suprimentos indiretos/Empreendedor em Ascenção": {  
        "modelo": "EMPREENDEDOR EM ASCENSÃO.png",
        "output": "AVD24.1/retaguarda/suprimentos_indiretos/empreendedor_ascensão"
    },
    "Retaguarda/Suprimentos indiretos/Empreendedor Potencial": {  
        "modelo": "EMPREENDEDOR EM POTENCIAL.png",
        "output": "AVD24.1/retaguarda/suprimentos_indiretos/empreendedor_potencial"
    },
    "Retaguarda/Suprimentos indiretos/Empreendedor Aprendiz": {  
        "modelo": "EMPREENDEDOR APRENDIZ.png",
        "output": "AVD24.1/retaguarda/suprimentos_indiretos/empreendedor_aprendiz"
    },
    "Retaguarda/Tecnologia de Operações/Empreendedor Aprendiz": {  
        "modelo": "EMPREENDEDOR APRENDIZ.png",
        "output": "AVD24.1/retaguarda/tecnologia_operacoes/empreendedor_aprendiz"
    },
    "Retaguarda/Tecnologia de Operações/Empreendedor em Ascenção": {  
        "modelo": "EMPREENDEDOR EM ASCENSÃO.png",
        "output": "AVD24.1/retaguarda/tecnologia_operacoes/empreendedor_ascensão"
    },
    "Retaguarda/Tecnologia de Operações/Empreendedor Potencial": {  
        "modelo": "EMPREENDEDOR EM POTENCIAL.png",
        "output": "AVD24.1/retaguarda/tecnologia_operacoes/empreendedor_potencial"
    },
    "Retaguarda/TEX/Empreendedor Potencial": {  
        "modelo": "EMPREENDEDOR EM POTENCIAL.png",
        "output": "AVD24.1/retaguarda/tex/empreendedor_potencial"
    },
    "Retaguarda/TEX/Empreendedor Aprendiz": {  
        "modelo": "EMPREENDEDOR APRENDIZ.png",
        "output": "AVD24.1/retaguarda/tex/empreendedor_aprendiz"
    },
    "Retaguarda/TEX/Empreendedor em Ascenção": {  
        "modelo": "EMPREENDEDOR EM ASCENSÃO.png",
        "output": "AVD24.1/retaguarda/tex/empreendedor_ascensão"
    },
    "São Luís/Empreendedor em Ascensão": {  
        "modelo": "EMPREENDEDOR EM ASCENSÃO.png",
        "output": "AVD24.1/sao_luis/empreendedor_ascensão/"
    },
    "São Luís/Empreendedor Potencial": {  
        "modelo": "EMPREENDEDOR EM POTENCIAL.png",
        "output": "AVD24.1/sao_luis/empreendedor_potencial/"
    },
    "São Luís/Empreendedor Aprendiz": {  
        "modelo": "EMPREENDEDOR APRENDIZ.png",
        "output": "AVD24.1/sao_luis/empreendedor_aprendiz/"
    },
}

base_fotos_path = "imagens/"
escala_foto = 0.45
font_path = "C:/Windows/Fonts/COPRGTB.ttf"
font_size = 30
font = ImageFont.truetype(font_path, font_size)

def colocar_foto_no_modelo(foto_path, modelo, escala_foto, nome):
    foto = Image.open(foto_path)
    foto_largura, foto_altura = foto.size

    nova_largura = int(modelo_largura * escala_foto)
    nova_altura = int(foto_altura * (nova_largura / foto_largura))

    foto_redimensionada = foto.resize((nova_largura, nova_altura))

    x = (modelo_largura - nova_largura) // 2
    y = (modelo_altura - nova_altura) // 2

    modelo_com_foto = modelo.copy()
    modelo_com_foto.paste(foto_redimensionada, (x, y), foto_redimensionada.convert('RGBA'))

    draw = ImageDraw.Draw(modelo_com_foto)

    text_bbox = draw.textbbox((0, 0), nome, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    text_x = (modelo_largura - text_width) // 2
    text_y = modelo_altura - text_height - 220

    draw.text((text_x, text_y), nome, font=font, fill="white")

    return modelo_com_foto

for pasta_fotos, info in modelos_por_pasta.items():
    fotos_path = os.path.join(base_fotos_path, pasta_fotos)
    output_path = info["output"]

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    modelo = Image.open(info["modelo"])
    modelo_largura, modelo_altura = modelo.size

    for foto_filename in os.listdir(fotos_path):
        if foto_filename.endswith(('.png', '.jpg', '.jpeg', 'webp', '.webp')):
            foto_path = os.path.join(fotos_path, foto_filename)

            nome_completo = os.path.splitext(foto_filename)[0]
            nomes = nome_completo.split()

            if len(nomes) > 3:
                nome = f"{nomes[0]} {nomes[1]} {nomes[2]}"
            else:
                nome = nome_completo

            modelo_final = colocar_foto_no_modelo(foto_path, modelo, escala_foto, nome)

            output_filename = os.path.join(output_path, f"{foto_filename}")
            modelo_final.save(output_filename, format='png')

            print(f"Foto {foto_filename} com nome {nome} inserida e salva como {output_filename}")



