<template>
  <table class = "infoSeason-table table-auto w-50 p-5" v-if="!loadingCharacter">
    <tbody>
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
            <div class="h-6 bg-orange-600 rounded-full dark:bg-blue-500 bg-orange-400 border-2 border-orange-800" role="progressbar"
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
</template>
<script>
export default {
  name: 'CharacterInfo',
  data() {
    return {
      character: null,
      loadingCharacter: true,
    }
  },
  methods: {
    getCharacterItems: async function() {
      try {
        let getCharacterLoggedAPI = await fetch('api/getCharacterLogged');
        let dataCharacterLogged = await getCharacterLoggedAPI.json();
        this.character = dataCharacterLogged.character
        let response = await fetch(`/api/getCharacter/`+this.character.id);
        let data = await response.json();
        this.character = data.character;
        this.loadingCharacter = false;
      } catch (error) {
        console.error(error);
        this.loadingCharacter = false;
      }
    },
    rechargeItems(){
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