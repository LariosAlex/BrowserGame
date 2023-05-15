import { createApp } from 'vue'
import RankingList from './components/GameRanking.vue'
import CharacterItems from './components/CharacterItems.vue'
import CharacterActions from './components/CharacterActions.vue'
import ActionButtons from './components/ActionsButtons.vue'
import CharacterInfo from './components/CharacterInformation.vue'
import CharacterLog from './components/CharacterLog'

createApp(RankingList).mount('#ranking')
createApp(CharacterItems).mount('#infoCharacter')
createApp(CharacterActions).mount('#actionsCharacter')
createApp(ActionButtons).mount('#actionButtons')
createApp(CharacterInfo).mount('#miniInformationCharacter')
createApp(CharacterLog).mount('#lastActionsCharacter')
