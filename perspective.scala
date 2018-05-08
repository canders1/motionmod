import com.cra.figaro.language.{Flip, Select}
import com.cra.figaro.library.compound.If
import com.cra.figaro.library.compound.^^
import com.cra.figaro.language._
import com.cra.figaro.library.collection.FixedSizeArray
import com.cra.figaro.library.atomic.discrete
import com.cra.figaro.util.random
import com.cra.figaro.patterns.learning._
import com.cra.figaro.library.atomic.continuous._
import com.cra.figaro.patterns.learning.ParameterCollection

object PerspectiveModel {

	def makeWorldProbs(numW : Int)={
		val p = 1.0/numW
		val wProbs = discrete.Uniform(0.until(numW).map(v => p): _*)
		wProbs
	}

	def makePerspectiveProbs(numP : Int)={
		val p = 1.0/numP
		val pProbs = Dirichlet(0.until(numP).map(v => p): _*)
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

	/*def sampleWorld(worldList:List[Map[String,Boolean]],wProbs:IndexedSeq[Double]) = {
		val world = Select(0.until(worldList.length-1).map(v => wProbs(v) -> v): _*)
		world
	}

	def samplePerspective(perspectives:List[String],pProbs:IndexedSeq[Double]) = {
		val perspective = Select(0.until(perspectives.length-1).map(v => pProbs(v) -> v): _*)
		perspective
	}

	def literalListener(utterance: String, perspective:String, worldList:List[Map[String,Boolean]],wProbs:IndexedSeq[AtomicSelect[Int]]) = {
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

	def literalSpeaker(worldIndex:Int,perspective:String,worldList:List[Map[String,Boolean]],wProbs:IndexedSeq[AtomicSelect[Int]], utterances:List[String]) = {
		println(utterances)
		val uttUtil = for (u <- utterances) yield {
			println(literalListener(u,perspective,worldList,wProbs))
			literalListener(u,perspective,worldList,wProbs)(worldIndex)
		}
		println(uttUtil)
		val winner = uttUtil.indexOf(uttUtil.max)
		winner
	}

	def sampleLiteralSpeaker(worldList:List[Map[String,Boolean]],wProbs:IndexedSeq[Double],perspectives:List[String],pProbs:IndexedSeq[Double],utterances:List[String]) = {
		val p = samplePerspective(perspectives,pProbs)
		val w = sampleWorld(worldList,wProbs)
		val u = literalSpeaker(w,p,worldList,wProbs,pProbs,utterances)
		u
	}*/

	def main(args: Array[String]){
		val params = ModelParameters()
		val perspectives = makePerspectives()
		val pp = 1.0/perspectives.length
		val pProbs = Dirichlet(0.until(perspectives.length).map(v => pp): _*)("pProbs", params)
		val worldList = makeWorlds()
		val wp = 1.0/worldList.length
		val wProbs = discrete.Uniform(0.until(worldList.length).map(v => wp): _*)("wProbs", params)
		val utterances = makeUtterances()
		
		//val pProbs = makePerspectiveProbs(perspectives.length)
		println(pProbs)
		/*val truth = getTruthValue("I am coming to Northampton",worldList(worldList.length-3),perspectives(1))
		val lit = literalListener("I am coming to Northampton",perspectives(0),worldList,wProbs)
		val utterance= literalSpeaker(worldList.length-3,perspectives(0),worldList,wProbs,pProbs,utterances)
		println(utterance)*/
	}
}