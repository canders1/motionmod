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
		val worldList = List(
		Map("inNohoSarah" -> true, "inNohoJane"-> true, "moveJaneNoho"-> false, "moveSarahNoho"-> false, "moveElizaNoho"-> true),
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
		utterance match {
			case "Eliza is coming to Northampton" => if(world("moveElizaNoho") && (perspective=="Sarah"&&world("inNohoSarah") ||(perspective=="Jane"&&world("inNohoJane")))) 1; else 0
			case "Eliza is going to Northampton" => if(world("moveElizaNoho") && (perspective=="Sarah"&&(world("inNohoSarah")==false) ||(perspective=="Jane"&&(world("inNohoJane")==false)))) 1; else 0
			case "You are coming to Northampton" => if(world("moveJaneNoho")&&perspective=="Sarah"&&world("inNohoSarah")) 1; else 0
			case "I am coming to Northampton" => if(world("moveSarahNoho")&&perspective=="Jane"&&world("inNohoJane")) 1; else 0
		}
	}

	def literalListener(utterance: String, perspective:String, worldList:List[Map[String,Boolean]],wProbs:IndexedSeq[Double]) = {
		val postW = for (w <- 0 until worldList.length) yield {
			getTruthValue(utterance,worldList(w),perspective)*wProbs(w)
		}
		val norm = postW.sum
		if(norm > 0){
		val normPostW = for (w <- postW) yield {
			w/norm
		}
		normPostW}; else postW
	}

	def literalSpeaker(worldIndex:Int,perspective:String,worldList:List[Map[String,Boolean]],wProbs:IndexedSeq[Double],pProbs:IndexedSeq[Double], utterances:List[String]) = {
		println(utterances)
		val uttUtil = for (u <- utterances) yield {
			println(literalListener(u,perspective,worldList,wProbs))
			literalListener(u,perspective,worldList,wProbs)(worldIndex)
		}
		println(uttUtil)
		val winner = uttUtil.indexOf(uttUtil.max)
		winner
	}

	def main(args: Array[String]){
		val worldList = makeWorlds()
		val wProbs = makeWorldProbs(worldList.length)
		val utterances = makeUtterances()
		val perspectives = makePerspectives()
		val pProbs = makePerspectiveProbs(perspectives.length)
		val truth = getTruthValue("I am coming to Northampton",worldList(worldList.length-3),perspectives(1))
		val lit = literalListener("I am coming to Northampton",perspectives(0),worldList,wProbs)
		val utterance= literalSpeaker(worldList.length-3,perspectives(0),worldList,wProbs,pProbs,utterances)
		println(utterance)
	}
}