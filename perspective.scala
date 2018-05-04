import com.cra.figaro.language.{Flip, Select}
import com.cra.figaro.library.compound.If
import com.cra.figaro.library.compound.^^
import com.cra.figaro.language._
import com.cra.figaro.library.collection.FixedSizeArray
import com.cra.figaro.library.atomic.discrete

object PerspectiveModel {

	def makeWorldProbs(numW : Int)={
		val wProbs = for(w <- 0 until numW) yield {
			1.0/numW
		}
		wProbs
	}

	def makePerspectiveProbs(numP : Int)={
		val pProbs = for(p <- 0 until numP) yield {
			1.0/numP
		}
		pProbs
	}

	def makeUtterances()={
		val utterances = List("You are coming to Northampton","I am coming to Northampton","Eliza is going to Northampton","Eliza is coming to Northampton")
		utterances
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

	def makePerspectives()={
		val speaker = "Sarah"
		val addressee = "Jane"
		val perspectives = List(speaker,addressee)
		perspectives
	}

	def getTruthValue(utterance: String, world:Map[String,Boolean],perspective:String)={

	}

	def main(args: Array[String]){
		val worldList = makeWorlds()
		val wProbs = makeWorldProbs(worldList.length)
		val utterances = makeUtterances()
		val perspectives = makePerspectives()
		val pProbs = makePerspectiveProbs(perspectives.length)
		getTruthValue(utterances(0),worldList(0),perspectives(0))
	}
}