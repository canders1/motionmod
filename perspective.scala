import com.cra.figaro.language.{Flip, Select}
import com.cra.figaro.library.compound.If
import com.cra.figaro.library.compound.^^
import com.cra.figaro.language._
import com.cra.figaro.library.collection.FixedSizeArray

object PerspectiveModel {

	def makeWorldProbs(numW : int)={
		wProbs = Array()
		for(w <- 0 until numW){

		}

	}

	def makeWorlds()={
		val worldList = List(Map("inNohoSarah" -> true, "inNohoJane"-> true, "moveJaneNoho"-> false, "moveSarahNoho"-> false, "moveElizaNoho"-> true),
		Map("inNohoSarah"-> false, "inNohoJane"-> true, "moveJaneNoho"-> false, "moveSarahNoho"-> false, "moveElizaNoho"-> true),
		Map("inNohoSarah"-> true, "inNohoJane"-> false, "moveJaneNoho"-> false, "moveSarahNoho"-> false, "moveElizaNoho"-> true),
		Map("inNohoSarah"-> false, "inNohoJane"-> false, "moveJaneNoho"-> false, "moveSarahNoho"-> false, "moveElizaNoho"-> true),
		Map("inNohoSarah"-> true, "inNohoJane"-> true, "moveJaneNoho"-> false, "moveSarahNoho"-> false, "moveElizaNoho"-> false),
		Map("inNohoSarah"-> false, "inNohoJane"-> true, "moveJaneNoho"-> false, "moveSarahNoho"-> false, "moveElizaNoho"-> false),
		Map("inNohoSarah"-> true, "inNohoJane"-> false, "moveJaneNoho"-> false, "moveSarahNoho"-> false, "moveElizaNoho"-> false),
		Map("inNohoSarah"-> false, "inNohoJane"-> false, "moveJaneNoho"-> false, "moveSarahNoho"-> false, "moveElizaNoho"-> false),
		Map("inNohoSarah"-> false, "inNohoJane"-> true, "moveJaneNoho"-> false, "moveSarahNoho"-> true, "moveElizaNoho"-> true),
		Map("inNohoSarah"-> false, "inNohoJane"-> true, "moveJaneNoho"-> false, "moveSarahNoho"-> true, "moveElizaNoho"-> false),
		Map("inNohoSarah"-> false, "inNohoJane"-> false, "moveJaneNoho"-> false, "moveSarahNoho"-> true, "moveElizaNoho"-> true),
		Map("inNohoSarah"-> false, "inNohoJane"-> false, "moveJaneNoho"-> false, "moveSarahNoho"-> true, "moveElizaNoho"-> false),
		Map("inNohoSarah"-> true, "inNohoJane"-> false, "moveJaneNoho"-> true, "moveSarahNoho"-> false, "moveElizaNoho"-> true),
		Map("inNohoSarah"-> true, "inNohoJane"-> false, "moveJaneNoho"-> true, "moveSarahNoho"-> false, "moveElizaNoho"-> false),
		Map("inNohoSarah"-> false, "inNohoJane"-> false, "moveJaneNoho"-> true, "moveSarahNoho"-> false, "moveElizaNoho"-> true),
		Map("inNohoSarah"-> false, "inNohoJane"-> false, "moveJaneNoho"-> true, "moveSarahNoho"-> false, "moveElizaNoho"-> false))
		worldList
	}

	def main(args: Array[String]){
		val worldList = makeWorlds()

	}
}