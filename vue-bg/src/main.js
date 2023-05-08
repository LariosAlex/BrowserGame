import { createApp } from 'vue'
import RankingList from './components/GameRanking.vue'
import CharacterItems from './components/CharacterItems.vue'
import CharacterActions from './components/CharacterActions.vue'

createApp(RankingList).mount('#ranking')
createApp(CharacterItems).mount('#infoCharacter')
createApp(CharacterActions).mount('#actionsCharacter')