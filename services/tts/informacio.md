## 📄 Informació
TTS natural i eficient en català: 🍵+🥑

Aquí trobareu tota la informació sobre els nostres models 🍵 Matxa i 🥑 alVoCat, que han estat entrenats mitjançant aprenentatge profund (_deep learning_).
Si voleu informació específica sobre com entrenar aquests models, podeu trobar-la [aquí](https://huggingface.co/BSC-LT/matcha-tts-cat-multiaccent) i [aquí](https://huggingface.co/BSC-LT/vocos-mel-22khz-cat) respectivament. 
El codi que hem utilitzat també es troba a Github [aquí](https://github.com/langtech-bsc/Matcha-TTS/tree/dev-cat).

## Taula de continguts
<details>
<summary>Feu clic per expandir</summary>

- [Descripció general del model](#descripció-general-del-model)
- [Usos previstos i limitacions](#usos-previstos-i-limitacions)
- [Mostres](#mostres)
- [Components principals](#components-principals)
- [El model en detall](#el-model-en-detall)
- [Adaptació al català](#adaptació-al-català)
- [Citació](#citació)  
- [Informació adicional](#informació-adicional)

</details>

## Descripció general del model

La importància de les tecnologies de síntesi de parla (TTS, per les seves sigles en anglès) de codi obert per a les llengües minoritàries no pot ser negligida. 
Aquestes tecnologies democratitzen l'accés a les solucions de TTS, proporcionant un marc perquè les comunitats desenvolupin i adaptin models segons les seves necessitats lingüístiques. 
Per això, utilitzant un conjunt de tecnologies, hem desenvolupat diferents solucions de TTS de codi obert i en català.

Us presentem 🍵 Matxa, el primer model TTS neuronal multiparlant i multidialectal. 
Es combina amb el model vocoder 🥑 alVoCat per generar unes veus expressives i d'alta qualitat. 
A més, funciona de manera eficient en quatre dialectes:

* Balear
* Central
* Nord-occidental
* Valencià

Tant 🍵 Matxa com 🥑 alVoCat s'ha entrenat amb dades obertes.

Els models 🍵 Matxa són lliures per utilitzar-los amb finalitats no comercials, mentre que l'ús comercial necessita una llicència directament del locutor/a. 
Trobareu més informació sobre aquesta qüestió a la secció [Llicència](#informació-adicional) i a la [pàgina del model](https://huggingface.co/BSC-LT/matcha-tts-cat-multiaccent/).

## Usos previstos i limitacions

Aquest model serveix com a generador de característiques acústiques per a sistemes de text-a-veu multi-parlant per a la llengua catalana.
Ha estat ajustat mitjançant un fonemitzador català; per tant, si el model s'utilitza amb altres llengües, pot ser que produeixi mostres inintel·ligibles.

La qualitat de les mostres pot variar segons el locutor.
Això pot ser degut tant a causa de la sensibilitat del model a l'hora d'aprendre certes freqüències específiques com de la qualitat de les mostres de cada locutor.

## Exemples
* Veus femenines:

<table style="font-size:16px">
  <col width="205">
  <col width="205">
  <td>Valencià</td>
  <td>Nord-Occidental</td>
  <td>Balear</td>
<tbody
<table>
  <tbody>
    <tr>
      <td>
        <audio controls="" preload="none" style="width: 200px">
          audio not supported
          <source src="https://github.com/mllopartbsc/assets/raw/c6a393237e712851dd7cc7d10c70dde29d3412ac/matcha_tts_catalan/valencia/spk1/0.wav" type="audio/wav">
        </audio>
      </td>
      <td>
        <audio controls="" preload="none" style="width: 200px">
          audio not supported
          <source src="https://github.com/mllopartbsc/assets/raw/c6a393237e712851dd7cc7d10c70dde29d3412ac/matcha_tts_catalan/occidental/spk1/0.wav" type="audio/wav"">
        </audio>
      </td>
      <td>
        <audio controls="" preload="none" style="width: 200px">
          audio not supported
          <source src="https://github.com/mllopartbsc/assets/raw/c6a393237e712851dd7cc7d10c70dde29d3412ac/matcha_tts_catalan/balear/spk1/0.wav" type="audio/wav">
        </audio>
      </td>
    </tr>
    <tr>
      <td>
        <audio controls="" preload="none" style="width: 200px">
          audio not supported
          <source src="https://github.com/mllopartbsc/assets/raw/c6a393237e712851dd7cc7d10c70dde29d3412ac/matcha_tts_catalan/valencia/spk1/1.wav" type="audio/wav">
        </audio>
      </td>
      <td>
        <audio controls="" preload="none" style="width: 200px">
          audio not supported
          <source src="https://github.com/mllopartbsc/assets/raw/c6a393237e712851dd7cc7d10c70dde29d3412ac/matcha_tts_catalan/occidental/spk1/1.wav" type="audio/wav">
        </audio>
      </td>
      <td>
        <audio controls="" preload="none" style="width: 200px">
          audio not supported
          <source src="https://github.com/mllopartbsc/assets/raw/c6a393237e712851dd7cc7d10c70dde29d3412ac/matcha_tts_catalan/balear/spk1/1.wav" type="audio/wav">
        </audio>
      </td>
    </tr>
    <tr>
      <td>
        <audio controls="" preload="none" style="width: 200px">
          audio not supported
          <source src="https://github.com/mllopartbsc/assets/raw/c6a393237e712851dd7cc7d10c70dde29d3412ac/matcha_tts_catalan/valencia/spk1/2.wav" type="audio/wav">
        </audio>
      </td>
      <td>
        <audio controls="" preload="none" style="width: 200px">
          audio not supported
          <source src="https://github.com/mllopartbsc/assets/raw/c6a393237e712851dd7cc7d10c70dde29d3412ac/matcha_tts_catalan/occidental/spk1/2.wav" type="audio/wav">
        </audio>
      </td>
      <td>
        <audio controls="" preload="none" style="width: 200px">
          audio not supported
          <source src="https://github.com/mllopartbsc/assets/raw/c6a393237e712851dd7cc7d10c70dde29d3412ac/matcha_tts_catalan/balear/spk1/2.wav" type="audio/wav">
        </audio>
      </td>
    </tr>
  </tbody>
</table>

* Veus masculines:

<table style="font-size:16px">
  <col width="205">
  <col width="205">
<thead>
<tr>
  <td>Valencià</td>
  <td>Nord-Occidental</td>
  <td>Balear</td>
</tr>
</thead>
<tbody
<table>
  <tbody>
    <tr>
      <td>
        <audio controls="" preload="none" style="width: 200px">
          audio not supported
          <source src="https://github.com/mllopartbsc/assets/raw/c6a393237e712851dd7cc7d10c70dde29d3412ac/matcha_tts_catalan/valencia/spk0/0.wav" type="audio/wav">
        </audio>
      </td>
      <td>
        <audio controls="" preload="none" style="width: 200px">
          audio not supported
          <source src="https://github.com/mllopartbsc/assets/raw/c6a393237e712851dd7cc7d10c70dde29d3412ac/matcha_tts_catalan/occidental/spk0/0.wav" type="audio/wav"">
        </audio>
      </td>
      <td>
        <audio controls="" preload="none" style="width: 200px">
          audio not supported
          <source src="https://github.com/mllopartbsc/assets/raw/c6a393237e712851dd7cc7d10c70dde29d3412ac/matcha_tts_catalan/balear/spk0/0.wav" type="audio/wav">
        </audio>
      </td>
    </tr>
    <tr>
      <td>
        <audio controls="" preload="none" style="width: 200px">
          audio not supported
          <source src="https://github.com/mllopartbsc/assets/raw/c6a393237e712851dd7cc7d10c70dde29d3412ac/matcha_tts_catalan/valencia/spk0/1.wav" type="audio/wav">
        </audio>
      </td>
      <td>
        <audio controls="" preload="none" style="width: 200px">
          audio not supported
          <source src="https://github.com/mllopartbsc/assets/raw/c6a393237e712851dd7cc7d10c70dde29d3412ac/matcha_tts_catalan/occidental/spk0/1.wav" type="audio/wav">
        </audio>
      </td>
      <td>
        <audio controls="" preload="none" style="width: 200px">
          audio not supported
          <source src="https://github.com/mllopartbsc/assets/raw/c6a393237e712851dd7cc7d10c70dde29d3412ac/matcha_tts_catalan/balear/spk0/1.wav" type="audio/wav">
        </audio>
      </td>
    </tr>
    <tr>
      <td>
        <audio controls="" preload="none" style="width: 200px">
          audio not supported
          <source src="https://github.com/mllopartbsc/assets/raw/c6a393237e712851dd7cc7d10c70dde29d3412ac/matcha_tts_catalan/valencia/spk0/2.wav" type="audio/wav">
        </audio>
      </td>
      <td>
        <audio controls="" preload="none" style="width: 200px">
          audio not supported
          <source src="https://github.com/mllopartbsc/assets/raw/c6a393237e712851dd7cc7d10c70dde29d3412ac/matcha_tts_catalan/occidental/spk0/2.wav" type="audio/wav">
        </audio>
      </td>
      <td>
        <audio controls="" preload="none" style="width: 200px">
          audio not supported
          <source src="https://github.com/mllopartbsc/assets/raw/c6a393237e712851dd7cc7d10c70dde29d3412ac/matcha_tts_catalan/balear/spk0/2.wav" type="audio/wav">
        </audio>
      </td>
    </tr>
  </tbody>
</table>

## Components principals

El nostre model de síntesi de parla adaptat al català utilitza un procés en diferents etapes per a convertir el text escrit en paraules ben pronunciades. Aquestes són les etapes:

1- Inicialment, el model analitza el text d'entrada, descomponent-lo en unitats lingüístiques més petites, com ara paraules i frases. 
També identifica els caràcters especials. Tot seguit, utilitza la nostra versió d'eSpeak, un fonemitzador basat en les regles fonètiques de la llengua catalana, per a transcriure el text fonèticament. Per a cada accent català, s'apliquen certes regles d'eSpeak específicament adaptades.

2- El model matcha-TTS converteix aquests fonemes en un mel-espectrograma, una representació visual de l'espectre de freqüències d'un so al llarg del temps. 

3- A continuació, aquest espectrograma s'afegeix com a input a [la nostra adaptació del vocoder Vocos](https://huggingface.co/BSC-LT/vocos-mel-22khz-cat), que sintetitza l'ona sonora.

Emprant aquesta sèrie d'etapes, el model de TTS assegura una pronunciació precisa i un discurs en català de so natural adaptat als matisos de la llengua. 
El còmput d'aquestes etapes va ser realitzat pel Marenostrum 5 del Centre Nacional de Supercomputació de Barcelona, i pel Finisterrae III de CESGA.

Aquestes tecnologies formen, conjuntament, una solució TTS completa, adaptada a les necessitats dels parlants de català i que exemplifica el poder de les iniciatives de codi obert per avançar en la diversitat lingüística i la inclusió.

## El model en detall

**Matcha-TTS** és una arquitectura d'_encoder-decoder_ dissenyada per a una modelització acústica ràpida en TTS.
D'una banda, la part de l'_encoder_ es basa en un codificador de text i una predicció de duració fonètica. 
Junts, prediuen una mitjana de les característiques acústiques.
D'altra banda, el _decoder_ té bàsicament un esquelet U-Net inspirat en [Grad-TTS](https://arxiv.org/pdf/2105.06337.pdf), 
que es basa en l'arquitectura Transformer.
En aquest últim, substituint CNNs 2D per CNNs 1D, s'aconsegueix una gran reducció en el consum de memòria i una síntesi ràpida.

**Matcha-TTS** és un model no autoregressiu entrenat amb emparellament de flux condicional d'optimització de transport (OT-CFM).
Això produeix un decodificador basat en ODE capaç de generar una alta qualitat de sortida en menys passos de síntesi que els models entrenats 
utilitzant score matching.

## Adaptació al català

El model original de Matcha-TTS excel·leix en anglès, però per adaptar-lo al català, hem dut a terme un procés multi-etapa. 
En primer lloc, hem fet el _fine-tuning_ del model d'anglès al català creant un Matxa-base, fent servir un subconjunt de 100h de la base de dades del català de [CommonVoice](https://commonvoice.mozilla.org/es/datasets) v.16.
La tria d'aquest petit conjunt de mostres s'ha realitzat de manera automàtica amb l'ajuda del sistema [UTMOS](https://arxiv.org/abs/2204.02152), un predictor de valors de la mètrica _Mean Opinion Score_ (MOS), una puntuació que solen fixar avaluadors humans segons la seva percepció subjectiva de la qualitat de la parla.

A continuació, hem fet un altre _fine-tuning_ de Matxa-base amb el conjunt de dades LaFresCat per introduir les variants dialectals. 
Aquest conjunt dades, que es publicarà aviat, té 3,5 hores d'enregistraments per a quatre variants dialectals:

 * Balear

 * Central
 
 * Nord-Occidental
 
 * Valencià
 
Amb un locutor masculí i un femení per a cada dialecte.

Després, mitjançant l'ajustament per a aquests dialectes catalans específics, el model es va adaptar a les variacions dialectals de pronúncia i prosòdia. 
Aquest enfocament meticulós garanteix que el model reflecteixi la riquesa lingüística i la diversitat cultural dins de la comunitat de parla catalana, oferint una comunicació fluida entre dialectes que prèviament no comptaven amb aquestes tecnologies.

A més de l'entrenament del model Matcha-TTS per al català, la integració del fonemitzador d'eSpeak ha jugat un paper crucial en millorar la naturalitat i l'exactitud de la parla generada. 
Un sistema TTS consta de diversos components, cadascun dels quals contribueix a la qualitat global de la parla sintetitzada. 
El primer component implica el pre-processament de text, on el text d'entrada es normalitza i s'analitza lingüísticament per identificar paraules, puntuació i característiques lingüístiques. 
A continuació, el text es converteix en fonemes, les unitats més petites de so en una llengua, a través d'un procés anomenat fonemització. 
Aquest pas és on el fonemitzador d'eSpeak destaca, ja que converteix amb precisió el text català en representacions fonètiques, capturant els subtils matisos de pronunciació específics del català. 
Podeu trobar la versió d'eSpeak que vam utilitzar [aquí](https://github.com/projecte-aina/espeak-ng/tree/dev-ca).

Després de la fonemització, els fonemes es passen al component de síntesi, on es transformen en parla audible. 
Aquí, el model Matxa pren protagonisme, generant una parla fluida i natural a partir de les representacions fonètiques. 
L'ús d'un model de TTS entrenat específicament per al català, juntament amb el fonemitzador d'eSpeak, assegura una pronunciació precisa i una parla coherent, capturant la riquesa i la diversitat del català en tots els seus dialectes i varietats.

Finalment, el discurs sintetitzat passa per un post-processament, on s'apliquen característiques prosòdiques com el to, la durada i l'èmfasi per refinar encara més la sortida i fer-la sonar més natural i expressiva. 
Integrant el fonemitzador d'eSpeak en el flux de treball del TTS i adaptant-lo al català, juntament amb l'entrenament del model Matcha-TTS per al català, hem creat un sistema complet i efectiu per generar parla catalana de alta qualitat. 
Aquesta combinació de tècniques avançades i atenció meticulosa als detalls lingüístics és imprescindible per superar les barreres lingüístiques i facilitar la comunicació per als parlants de català arreu del món.

## Citació

Si feu servir el model per a la vostra recerca o projecte, us agrairem que citeu el següent paper:

```
@misc{LTU2024,
  title={Natural and efficient TTS in Catalan: using Matcha-TTS with the Catalan language},
  author={The Language Technologies Unit from Barcelona Supercomputing Center},
  year={2024},
}
```
```
@misc{mehta2024matchatts,
      title={Matcha-TTS: A fast TTS architecture with conditional flow matching}, 
      author={Shivam Mehta and Ruibo Tu and Jonas Beskow and Éva Székely and Gustav Eje Henter},
      year={2024},
      eprint={2309.03199},
      archivePrefix={arXiv},
      primaryClass={eess.AS}
}
```

## Informació addicional

### Autor
Unitat de Tecnologies del Llenguatge del Centre Nacional de Supercomputació de Barcelona.

### Contacte
Per a més informació, si us plau, envia un correu electrònic a <langtech@bsc.es>.

### Copyright
Copyright(c) 2023 by Language Technologies Unit, Barcelona Supercomputing Center.

### Llicència
Aquesta pàgina de demostració i els scripts d'inferència es troben sota [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)

Els pesos del model tenen la llicència [Creative Commons Attribution Non-comercial 4.0](https://www.creativecommons.org/licenses/by-nc/4.0/). Aquests models són lliures per l'ús no comercial i d'investigació. L'ús comercial és possible mitjançant una llicència directe amb el locutor/la locutora. Per a més informació, contacteu amb <langtech@bsc.es> i <lafrescaproduccions@gmail.com>. Per obtenir més informació, consulteu la [pàgina del model](https://huggingface.co/BSC-LT/matcha-tts-cat-multiaccent/).

### Finançament
Aquest treball ha estat promogut i finançat per la Generalitat de Catalunya a través del [Projecte Aina](https://projecteaina.cat/).

Una part de l'entrenament dels models va ser possible gràcies al temps de comput proporcionat pel [Centro de Supercomputación de Galicia (CESGA)](https://www.cesga.es/) i també pel [Barcelona Supercomputing Center](https://www.bsc.es/) amb el seu MareNostrum 5.