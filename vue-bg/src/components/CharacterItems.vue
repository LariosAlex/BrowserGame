<template>
  <table class = "infoSeason-table table-auto w-full p-5" v-if="!loadingCharacter">
    <thead>
          <tr>
          <th colspan="2"><h2>TEMPORADA {{ character.season }}</h2></th>
          </tr>
      </thead>
    <tbody>
      <tr>
        <th>NOM</th>
        <td>{{ character.nickname }}</td>
      </tr>
      <tr>
        <th>NIVELL</th>
        <td>{{ character.level }}</td>
      </tr>
      <tr>
        <td colspan="2">  
          <div class="flex justify-between mb-1">
            <span class="text-base font-medium text-blue-400 dark:text-white">EXPERIENCIA</span>
            <span class="text-base font-medium text-blue-400 dark:text-white">{{ (character.level * 10) }}</span>
          </div>       
          <div class="flex w-full h-6 bg-blue-200 rounded-full dark:bg-gray-700">
            <div class="h-6 bg-blue-600 rounded-full dark:bg-blue-500  bg-blue-400 border-2 border-blue-800" role="progressbar"
            :style="{width: ((((character.level * 10) - 0) > 0) ? (( character.exp  - 0) * 100) / ((character.level * 10) - 0) : 0) + '%'}"
            :aria-valuenow="character.exp" 
            :aria-valuemin="0" 
            :aria-valuemax="character.level * 10">{{ character.exp }}</div>
          </div>
        </td>
      </tr>
      <tr>
        <td colspan="2"> 
          <div class="flex justify-between mb-1">
            <span class="text-base font-medium text-orange-400 dark:text-white">MANÀ</span>
            <span class="text-base font-medium text-orange-400 dark:text-white">{{ (character.level * 10) }}</span>
          </div>       
          <div class="flex w-full h-6 bg-orange-200 rounded-full dark:bg-gray-700">
            <div class="h-6 bg-blue-600 rounded-full dark:bg-blue-500 bg-orange-400 border-2 border-orange-800" role="progressbar"
            :style="{width: ((((character.level * 10) - 0) > 0) ? (( character.mana  - 0) * 100) / ((character.level * 10) - 0) : 0) + '%'}"
            :aria-valuenow="character.mana" 
            :aria-valuemin="0" 
            :aria-valuemax="character.level * 10">{{ character.mana }}</div>
          </div>
        </td>
      </tr>
      <tr>
        <td colspan="2">
          <div class="flex justify-between mb-1">
            <span class="text-base font-medium text-green-400 dark:text-white">VIDA</span>
            <span class="text-base font-medium text-green-400 dark:text-white">{{ (character.level * 10) }}</span>
          </div>       
          <div class="flex w-full h-6 bg-green-200 rounded-full dark:bg-gray-700">
            <div class="h-6 bg-blue-600 rounded-full dark:bg-blue-500  bg-green-400 border-2 border-green-800" role="progressbar"
            :style="{width: ((((character.level * 10) - 0) > 0) ? (( character.life  - 0) * 100) / ((character.level * 10) - 0) : 0) + '%'}"
            :aria-valuenow="character.life" 
            :aria-valuemin="0" 
            :aria-valuemax="character.level * 10">{{ character.life }}</div>
          </div>
        </td>
      </tr>
    </tbody>
  </table>
  <table class="infoSeason-table table-auto w-full" v-else>
      <thead>
          <tr>
          <th colspan="3"><h2>CARREGANT PERSONATGE</h2></th>
          </tr>
      </thead>
    </table>
    <ActionButtons @recargar-items="rechargeItems" />
</template>
<script>
import ActionButtons from './ActionsButtons.vue'
export default {
  name: 'CharacterItems',
  data() {
    return {
      character: null,
      loadingCharacter: true,
    }
  },
  components:{ActionButtons, },
  methods: {
    getCharacterItems: async function() {
      try {
        const response = await fetch(`/api/getCharacter/`+this.character.characterLogged.id);
        const data = await response.json();
        this.character = data.character;
        this.loadingCharacter = false;
      } catch (error) {
        console.error(error);
        this.loadingCharacter = false;
      }
    },
    rechargeItems(){
      this.character = JSON.parse(document.getElementById('infoCharacter').getAttribute('data'));
      this.getCharacterItems();
    }
  },
  mounted() {
    this.rechargeItems()
    setInterval(() => {
      this.rechargeItems();
    }, 30000)
  },
}
</script>