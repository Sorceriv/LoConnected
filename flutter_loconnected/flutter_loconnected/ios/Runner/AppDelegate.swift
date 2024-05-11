import UIKit
import Flutter

@UIApplicationMain
@objc class AppDelegate: FlutterAppDelegate {
  override func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {
    GMSServices.provideAPIKey("AIzaSyBOaosExkcjs_RkXNSyOqeXyR5xzI6lKo4")
    GeneratedPluginRegistrant.register(with: self) 
    return super.application(application, didFinishLaunchingWithOptions: launchOptions)
  }
}
