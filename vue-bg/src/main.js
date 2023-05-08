import { createApp } from 'vue'
import RankingList from './components/GameRanking.vue'
import CharacterItems from './components/CharacterItems.vue'

createApp(RankingList).mount('#ranking')
createApp(CharacterItems).mount('#infoCharacter')